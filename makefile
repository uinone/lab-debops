start:
	pm2 start webhooks.py --name webhooks --interpreter python3
	pm2 start tcp-server.py --name tcp-server --interpreter python3 --watch
	pm2 save

stop:
	pm2 stop webhooks
	pm2 stop tcp-server


