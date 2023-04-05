
from flask_app import app   #Imports app
from flask_app.config.mysqlconnection import connectToMySQL #connects to DB
from flask_app.controllers import ninja_routes #connects routes
from flask_app.controllers import dojo_routes #connects routes

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
