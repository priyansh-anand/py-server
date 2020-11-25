# Expose Filesystem to local-network using Python

This python module exposes the filesystem to the local-network using flask with a beautiful front end (imo)

OS module is used where possible, so that it is not platform specfic, but some code has to be changed for it to work on Windows/Mac Machines. Contributors are welcome to do this too!

Currently, it is only tested on Linux system only

# How it looks

There are two views, you can toggle them using the button at the bottom right

![SS1](https://i.imgur.com/zjOGLH5.png)

![SS2](https://i.imgur.com/CbkBcnm.png)

![SS3](https://i.imgur.com/STKNaAM.jpeg)

![SS4](https://i.imgur.com/XjxMyPI.jpg)

# What can it do

You can browser/download files from the filesystem to any device on the local-network

You can also upload files/create folders too!

Note: Will add feature to delete files/folders too

# Installation

Follow the steps below to install this module globally on your system

```bash
git clone https://github.com/priyansh-anand/py-server
cd py-server
sudo pip3 install .
```

If your linux distribution uses systemd, you can follow the steps below to install the service to your linux distrubution, else you will have to do it manually

```bash
cd install-linux-systemd
chmod +x ./install.sh
chmod +x ./uninstall.sh
./install.sh
```

After you have installed the py-service on your linux distribution, you can start/stop it using these commands

```bash
sudo systemctl start py-server
sudo systemctl stop py-server
sudo systemctl status py-server
```

Now, after the service is running, you can use any device on your local network to access the file system of your pc. To access it, navigate to http://[YOUR-IP]:PORT in any browser
The default port is 6969. For configuration, you can check the section below.

## Configuration

The py-server is run as www-data user by default for safety purpose. But py-server can only access folders which can be accessed by www-data user. So, if you want to change the user, you can go the /etc/py-server/conf.ini

The default configuration is:

```ini
[py-server.conf]
PORT=6969
HOST='0.0.0.0'
WORKERS=2; Number of workers to run on the server
ASUSER=www-data; Run py-server as this user
```

You can change port, host, number of workers and the user py-server is run as.
Remember, you will have to restart the service, for the changes to be applied

# Security

**Don't use py-server on a public network such as a public wifi if you don't understand the risks of using HTTP on public networks**

Py-server runs on HTTP because it is running on the local-network. Using a website with HTTP means ANYONE can INTERCEPT/SPOOF the connection between your device and the server. If you want to avoid that, you can use self-signed SSL certificates, to avoid that. You can easily search 'how to use self-signed certificates for localhost' to find a tutorial on this topic.

I am working on a method to implement assymetric enryption, so that no one can spoof/intercept the communications even on HTTP, but it may take time to implement

# License

MIT
**Free Software, Hell Yeah!**

# Contribution

You are welcome to contribute if you want to!
Looking for devs to port this to Mac OS (Cuz I don't have Mac OS installed)
