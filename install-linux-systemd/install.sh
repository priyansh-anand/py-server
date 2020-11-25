cd "${0%/*}"
sudo mkdir -p /etc/py-server

sudo cp py-server.sh /etc/py-server
sudo cp conf.ini /etc/py-server
sudo chmod +x /etc/py-server/py-server.sh

sudo cp py-server.service /etc/systemd/system
sudo systemctl daemon-reload