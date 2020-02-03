# Innovation-Center
Innovation Center is the technology and business incubator of Manipal Academy of Higher Education(MAHE). In the university town of Manipal, many projects undertaken by students and professors become dead due to lack of technical support. For instance, students of Kasturba Medical College have an idea to develop a hardware equipment but have no technical knowledge to do it. Thus, this Django-based web application aims at reviving such projects by connecting students of various disciplines.

The project heads can register their team’s account on the website and after logging in to the portal, they can post offers and ask interested students to fill the Google Form which they have provided and thus the students would be contacted for the recruitments later. More features like deleting an offer, searching for all kind of offers provided by a particular company, time when the proposal was posted, etc. are included. 

This is just a basic prototype made by me so that the people concerned may have an idea of how exactly the application would function. 
 
## Technology Stack:
**Frontend**: HTML, CSS, Bootstrap4, Javascript <br/>
**Backend**: Python3, Django2

## How to run the application?
You need to follow these steps after cloning:
- Install python3 
- Install pip
- Install django2
- Install a text editor(preferably Atom or Sublime) to view the files.
- Run `npm install medium-editor` on the command line.
- Go to directory **blog_project** which has a file **manage.py**
- Run the following commands:
```python
    python manage.py migrate
    python manage.py makemigrations blog
    python manage.py migrate
    python manage.py runserver
```
- The output of the last command is an URL, you can use this URL to run the web application on your system locally.
