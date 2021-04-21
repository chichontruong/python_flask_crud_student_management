==============
python_flask_crud_student_management
==============

Building a CRUD application with Flask and SQLAlchemy


Requeriments
============

Please execute the following commands:

::

    $ git clone https://github.com/chichontruong/python_flask_crud_student_management.git
    $ cd ./flask-crud-app
    $ pip install -r requirements.txt


Running
=======

Please execute the following command:

::

    $ python app.py
     * Serving Flask app "app" (lazy loading)
     * Environment: production
       WARNING: Do not use the development server in a production environment.
       Use a production WSGI server instead.
     * Debug mode: on
     * Running on http://127.0.0.1:8087/ (Press CTRL+C to quit)
     * Restarting with stat
     * Debugger is active!
     * Debugger PIN: 245-060-649
    127.0.0.1 - - [04/Jul/2019 14:21:17] "GET / HTTP/1.1" 200 -
    127.0.0.1 - - [04/Jul/2019 14:21:18] "GET /favicon.ico HTTP/1.1" 404 -


Open at your Web browser the following link http://127.0.0.1:8087

SQLAlchemy to SQL
=================

**db.session.commit()**::

    INSERT INTO student (registration_number, name, email, date_of_birth, hometown, score) VALUES ('HTTT2025001', 'Trương Chí Chọn', 'chontc91@gmail.com', 'Kiên Giang', '10');
    INSERT INTO student (registration_number, name, email, date_of_birth, hometown, score) VALUES ('HTTT2025002', 'Trương Chí Chọn 1', 'chontc91@gmail.com', 'Kiên Giang', '10');
    INSERT INTO student (registration_number, name, email, date_of_birth, hometown, score) VALUES ('HTTT2025003', 'Trương Chí Chọn 2', 'chontc91@gmail.com', 'Kiên Giang', '10');
    INSERT INTO student (registration_number, name, email, date_of_birth, hometown, score) VALUES ('HTTT2025004', 'Trương Chí Chọn 3', 'chontc91@gmail.com', 'Kiên Giang', '10');
    COMMIT;

    UPDATE student
    SET name='Trương Chí Chọn 1'
    WHERE id = 1;
    COMMIT;

**Student.query.all()**::

    SELECT * FROM student;

**Student.query.filter_by(id=id).first()**::

    SELECT student.name
    FROM student
    WHERE student.id = 1
    LIMIT 1 OFFSET 0;

**db.session.delete(student)**::

    DELETE FROM student
    WHERE student.id = 1;


Reference
=========

- https://www.codementor.io/garethdwyer/building-a-crud-application-with-flask-and-sqlalchemy-dm3wv7yu2

- https://docs.sqlalchemy.org/en/latest/orm/tutorial.html

- http://flask-sqlalchemy.pocoo.org/2.3/queries/