cd "${0%/*}"
sudo rm -r /etc/py-server

sudo systemctl stop py-server
sudo rm /etc/systemd/system/py-server.service
sudo systemctl daemon-reload