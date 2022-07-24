# Poll (MaHa)

**This is a _Django Poll Project_ for `System Analysis & Design` course, developed by [Mohammadali Mojtahed Soleymani](https://github.com/mohammadalimojtahedsoleimani) and I.**

**In this Web application, If you don't have an account, you should `REGISTER`, first. else, you must `LOGIN`.
After that, you will redirect to poll index and you will be able to vote in favour of available polls.
Also, you can see the poll results. You can `LOGOUT`, at the end.**

![MaHa](https://user-images.githubusercontent.com/74541595/179214230-f8e5147f-029a-4e90-8adb-8d06ce3773ab.png)

## Installation

* First of all clone the project:
```
git clone https://github.com/EngRobot33/Poll.git
```
* Then, we need a virtual environment you can create like this:
```
virtualenv venv
```
* Activate it with the command below:
```
source venv/bin/activate
```
* After that, you must install all of the packages in `requirements.txt` file in project directory:
```
pip install -r requirements.txt
```
* Then you should have a superuser for accessing to admin panel:
```
python3 manage.py createsuperuser
```
* After that, migration:
```
python3 manage.py migrate
```
* That's finished now you can run the project:
```
python3 manage.py runserver
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
