# Running instructions:
    Ensure that you have Python with the PATH properly set and the Django library installed and execute the following in the terminal of your choice:
        python manage.py makemigrations aptman      //Builds database definition
        python manage.py migrate                    //Uses definition to build database
        python manage.py serverrun                  //Runs the server
    Unless a change to the database structure itself is made, makemigrations and migrate will only need to be run once

Once the server is running, you can navigate to http://127.0.0.1:8000/aptman to access the index

Note: Build was created and tested on a machine using 3.7.0, appears to be incompatible with 2.7