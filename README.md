# Spam reports REST API project
## Description
 Django REST framework project for updating the spamReportItem:
````$xslt
{
  "id": "01322891-c5cb-4ac5-90d4-3c4224f40ba2",
  "source": "REPORT",
  "sourceIdentityId": "d0ba4c4a-39da-4d2c-8934-80652da104fe",
  "reference": {
      "referenceId": "130debb9-cb13-49eb-881e-86fd3244639c",
      "referenceType": "REPORT"
  },
  "state": "OPEN",
  "payload": {
      "source": "REPORT",
      "reportType": "SPAM",
      "message": null,
      "reportId": "130debb9-cb13-49eb-881e-86fd3244639c",
      "referenceResourceId": "ba6f65d6-1a83-42bc-8839-ea2639faeb69",
      "referenceResourceType": "ARTICLE"
  },
  "created": "2017-10-30T14:34:06.569Z"
}
````
## Prerequisites
- [Django](http://www.django-rest-framework.org/tutorial/quickstart/)
- [djangoframework](http://www.django-rest-framework.org/tutorial/quickstart/)
- [Vagrant](https://www.vagrantup.com/)
- [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03)
- [VirtualBox](https://www.virtualbox.org/)

## Install instructions
- go to your workspace clone the repository and navigate to the new folder:
`````
> git clone git@github.com:gabriel-montagne/spam_reports_API.git (or http ...)
> cd spam_reports_API
`````
- run vagrant (wait until the VM is created):
```
> vagrant up
```
- connect to the VM:
```
> vagrant ssh
```
- create a new envirnoment (if it's already created activate it):
```
> mkvirtualenv spamreports_api
(> workon spamreports_api)
```
- go to vagrant folder:
```
> cd /vagrant
```
- instal requirements:
```
> pip install -r requirements.txt
```
- go to project folder:
```
> cd src/spam_reports_project/
```
- run the server:
```
> python manage.py runserver 0.0.0.0:8080
```
- open your browser and navigate to [localhost:8080/admin](localhost:8080/admin). Use the following credential to login
:
```
user: admin
pasword: asdf1234
(or you can create your own superuser using :
(spamreports_api) vagrant@ubuntu-xenial:/vagrant/src/spam_reports_project > python manage.py createsuperuser)
```
- navigate to [api/spamreports](localhost:8080/api/spamreports)
