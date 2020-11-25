function close_pop(ele_id) {
	document.getElementById(ele_id).style.display = "none";
	for (f of document.getElementsByTagName('form')) {
		f.reset();
	}

	document.getElementsByName("upload")[0].value = 'Upload';
	document.getElementById("cf_vb").innerHTML = 'Choose file';
	document.getElementsByName("upload")[0].style.backgroundImage = null;
}

function show_pop(ele_id) {
	document.getElementById(ele_id).style.display = "block";
}

function click_button(self, id) {
	document.getElementById(id).click();
}

function _change_view() {
	// unload css of one view type and load css of another view type
	document.getElementById("view0").disabled = !document.getElementById("view0").disabled;
	document.getElementById("view1").disabled = !document.getElementById("view1").disabled;
}

function change_view() {
	_change_view();
	if (localStorage.toggle == 'true') {
		localStorage.toggle = 'false';
	} else {
		localStorage.toggle = 'true';
	}
}


function submit_form(form, pop_id, progress_btn_name = null) {
	var xhr = new XMLHttpRequest();

	if (progress_btn_name != null) {
		xhr.upload.onprogress = function (e) {
			let perc = (e.loaded * 100 / e.total).toFixed(2) + "%";
			document.getElementsByName(progress_btn_name)[0].style.backgroundImage = "linear-gradient(to right, #99beff 0%, #99beff " + perc + ", #76A9FF " + perc + ")";
			document.getElementsByName(progress_btn_name)[0].value = "Uploading " + perc;

			if (perc == "100.00%") {
				document.getElementsByName(progress_btn_name)[0].style.backgroundColor = "#76A9FF";
				document.getElementsByName(progress_btn_name)[0].value = "Uploaded";
			}
		}

		document.getElementsByName(progress_btn_name)[0].disabled = true;
	}

	for (cancel of document.getElementsByName('cancel')) {
		cancel.addEventListener('click', function cancel_form() {
			this.removeEventListener('click', cancel_form, false);
			xhr.abort();
			form.reset();

			if (progress_btn_name != null) {
				document.getElementsByName(progress_btn_name)[0].disabled = false;
			}
		}, false);
	}

	xhr.onload = function () {
		close_pop(pop_id);
		form.reset();
		if (xhr.status != 200) {
			alert(xhr.responseText);
		}

		location.reload();
	};
	xhr.open(form.method, form.getAttribute("action"));
	xhr.send(new FormData(form));
	return false;
}


// Set either chosen view or the default one
document.getElementById("view1").disabled = true;
if (localStorage.toggle == 'true') {
	_change_view();
}

// setup "choose file" button on "choose file" popup
document.addEventListener("DOMContentLoaded", function () {
	document.getElementById("cf_inp").addEventListener("change", function (event) {
		let file = event.target.files;
		if (file.length > 0) {
			file = file[0].name;
			if (file.length > 0) {
				document.getElementById("cf_vb").innerText = file;
			}
		}
	}, false);
}, false)