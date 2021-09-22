# creating API for ml model and testing on postman

<1> create project on pycharm paste app.py and pipe.pkl in the project

<2> and run app.py file it generate url and copy that url

<3> download postman and login

<4> create new

<5>HTTP request

<6> change method to POST

<7>past copied url 

<8>click on body -> form-data and fill key and values from X_tain data

<9>code how i am give key and value

curl --location --request POST 'http://127.0.0.1:5000/predict' \
--form 'Company="Apple"' \
--form 'TypeName="Ultrabook"' \
--form 'Ram="8"' \
--form 'Weight="1.37"' \
--form 'Touchscreen="0"' \
--form 'Ips="1"' \
--form 'ppi="226.983005"' \
--form 'Cpu brand="Intel Core i5"' \
--form 'HDD="0"' \
--form 'SSD="128"' \
--form 'Gpu brand="Intel"' \
--form 'os="Mac"'

<10>then send
<11> then we will received 
{
    "price": 72265
}
<12>we get the price fron created api in JSON formate

![image](https://user-images.githubusercontent.com/66677660/134398624-fe669fac-ad2c-48f6-bd40-972fab563420.png)

<13> you can deploy that project in Heroku for commercial use of API

# Heroku Deploy

<1>first create this following file in your project
       1>procfile
         past-> web: gunicorn app:app
       
       2>requirement.txt
         flask 
         numpy
         sklearn
         gunicorn
<2>first make account in Heroku

<3>click on new app and remane app

<4>download Heroku cli and install

<5>Heroku specified command,run that command in cmd or terminal,while deploying also check correct project directory
