# Innovation-Center
Innovation Center is the technology and business incubator of Manipal Academy of Higher Education(MAHE). In the university town of Manipal, many projects undertaken by students and professors become dead due to lack of technical support. For instance, students of Kasturba Medical College have an idea to develop a hardware equipment but have no technical knowledge to do it. Thus, this Django-based web application aims at reviving such projects by connecting students of various disciplines.

The project heads can register their team’s account on the website and after logging in to the portal, they can post offers and ask interested students to fill the Google Form which they have provided and thus the students would be contacted for the recruitments later. More features like deleting an offer, searching for all kind of offers provided by a particular company, time when the proposal was posted, etc. are included. 

This is just a basic prototype made by me so that the people concerned may have an idea of how exactly the application would function. We’re planning to form a team of 3 developers to make a full-fledged website based on this idea which is expected to launch by the next academic year.
 
Technology Stack:
HTML, CSS and Bootstrap4 for frontend.
Python3 and Django2 for backend and server integration.

To using the project, you need to follow these steps after cloning:
1. Install python3 
2. Install django2
3. Install a text editor(preferably Atom or Sublime) to view the files.
4. Install pip
5. pip install libraries like misaka, django-boostrap4
6. Go to directory IC while has a file manage.py
7. Run 'python manage.py migrate' on the terminal
8. Run 'python manage.py makemigrations dashboard'
9. Run 'python manage.py makemigrations accounts'
10.Run 'python manage.py migrate' again
11.Run 'python manage.py runserver'
12.The output of the previous command is an URL, host the URL on your browser, now you use the web application.

