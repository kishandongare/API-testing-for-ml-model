# creating API for ml model and testing on postman

<1> create project on pycharm paste all except .ipynb and csv

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

<1>first make account in Heroku

<2>click on new app and remane app

<3>download Heroku cli and install

<4>Heroku specified command,run that command in cmd or terminal,while deploying also check correct project directory

<5>it generate URL you can use that url in postman for testing
