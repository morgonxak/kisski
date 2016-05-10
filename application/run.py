from app import app 
if __name__ =='__main__': 
	import os 
	host = os.environ.get('SERVER_HOST', 'localhost') 
	try:port = int(os.environ.get('SERVER_PORT', '5555')) 
	except ValueError: 
		port = 5555 
		app.run()
	else:
		app.config['ASSETS_DEBUG']=True
		app.run(debug = True)	
