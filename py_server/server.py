from flask import Flask, render_template, send_from_directory, session, redirect, request
import os
import urllib.parse

from .icons import get_icon

app = Flask(__name__)
app.secret_key = os.urandom(32)

root_path = os.getcwd()
root_path = "/"

show_hidden_files = True


@app.route("/")
def root():
    return get_dir(root_path)


@app.route("/<path:path>/")
def route(path):
    path = urllib.parse.unquote(path)
    _path = path

    # Convert the path to absolute path
    path = os.path.abspath(os.path.join(root_path, path))
    if os.path.islink(path):
        path = os.path.realpath(path)

    # If it is outside of the root directory allowed
    if not (root_path in path and path.index(root_path) == 0):
        return render_template("err.html", err="403 Forbidden", err_detail="You are not authorized to view this directory")

    if os.path.exists(path):
        if os.path.isdir(path):
            return get_dir(path)
        else:
            return get_file(_path)
    else:
        return render_template("err.html", err="404 Not found", err_detail="The requested file/directory is not found")


@app.route("/mkdir", methods=["POST"])
def mkdir():
    f_name = request.form.get('folder')
    root = request.form.get('red')

    try:
        os.mkdir(os.path.join(root, f_name))
        return "success", 200
    except PermissionError:
        return "You don't have sufficient permissions", 403
    except FileExistsError:
        return "File/Directory already exists", 409
    except:
        return "Cannot create directory", 500


@app.route("/upload", methods=["POST"])
def upload():
    f = request.files["file"]
    root = request.form.get("red")

    path = f.filename
    path = os.path.abspath(os.path.join(root, path))

    if os.path.exists(path):
        return "File already exists", 409

    if not (root_path in path and path.index(root_path) == 0):
        return "You don't have sufficient permissions", 403

    try:
        f.save(path)
        return "success", 200
    except PermissionError:
        return "You don't have sufficient permissions", 403
    except:
        return "Cannot upload file here", 500


def get_file_size(dir_path, file):
    # Return size of file in human readable format

    try:
        file = os.path.join(dir_path, file)
        s = os.stat(file).st_size
    except:
        return "-"

    sizes = ["B", "KB", "MB", "GB", "TB"]

    final_size = "%.2f" % s + " B"
    for i, size in enumerate(sizes):
        if s // 1024 ** i >= 1 or 1024 > s % 1024 ** i > 999:
            final_size = "%.2f" % (s / 1024 ** i) + " " + size

    return final_size


def get_dir_size(dir_path, dir):
    try:
        size = len(os.listdir(os.path.join(dir_path, dir)))
        if size > 999:
            size = "%.1fk" % (size / 1000)
        else:
            size = str(size)
        return size
    except:
        return "-"


def get_dir(dir_path):
    try:
        ls = os.listdir(dir_path)
    except PermissionError:
        return render_template("err.html", err="403 Forbidden", err_detail="You are not authorized to view this directory")

    if not show_hidden_files:
        ls = list(filter(lambda x: x[0] != ".", ls))

    # Get details of files in directory
    files = list(filter(lambda x: os.path.isfile(
        os.path.join(dir_path, x)), ls))
    files.sort()
    files = [(file, urllib.parse.quote(file), os.path.islink(os.path.join(
        dir_path, file)), get_icon(file), get_file_size(dir_path, file)) for file in files]

    # Get details of sub-directories in directory
    dirs = list(filter(lambda x: os.path.isdir(os.path.join(dir_path, x)), ls))
    dirs.sort()
    dirs = [(dir, urllib.parse.quote(dir), os.path.islink(os.path.join(
            dir_path, dir)), get_dir_size(dir_path, dir)) for dir in dirs]

    return render_template("main.html", dir_path=dir_path, dirs=dirs, files=files)


def get_file(file_path):
    return send_from_directory(root_path, file_path, as_attachment=True)
