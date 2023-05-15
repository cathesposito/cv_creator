# cv_creator
App to create CV pdfs from all user information.

# Instal Docker

For the project to work, you will need to have Docker installed.

After installing Docker, in the terminal, you must be at the same directory that the file "docker-compose.yaml" is, then:

    docker build .

When the build complete then type: 

    docker-compose up -d
    
# Migrate your database 

In the terminal move to where 'manage.py' file is and type:

    docker exec web python manage.py migrate
    
After migration you can create a super user using: 

    docker exec web python manage.py createsuperuser 

# App ready

The web application is ready to be used. Go to http://localhost:8000/. 

## Add objects

Go to http://localhost:8000/admin/

And add one object for 'Personal Information' about you. Then add at least one object for the other models.

The header image is located at 'cv_creator/media/images/5.png', so you can add in 'Personal Information' model in 'Image' field.

The you can go http://localhost:8000/cv_pdf_view/personal_info and click on 'Print CV'

