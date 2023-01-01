# An API for retreival of records. 
This project is built with Django and deployed on Railway.
The API is documented with Swagger - a UI interface that enables easier interaction with the API

1. Demo (hosted)
2. Local Setup


## 1. Demo (hosted)
link: https://certinfo-py.up.railway.app

The API contains list of certificates that can filtered and sorted.

The certificates has the following fields
- id
- certifcate_id
- full_name
- address
- dob
- type (nin, voter, driver)
- issued_on
- expired_on
- created 
- updated

  e.g

  https://certinfo-py.up.railway.app/api/v1/certificates

  returns a list of all records with the above fields.



The list can be filtered by the following fields
- id
- certifcate_id
- full_name
- address
- dob
- type (nin, voter, driver)

    e.g

    https://certinfo-py.up.railway.app/api/v1/certificates?id=3
    https://certinfo-py.up.railway.app/api/v1/certificates?certificated_id=00001A



A text search can be done accross the following fields
- id
- certifcate_id
- full_name
- address
- dob
- type (nin, voter, driver)

    e.g

    https://certinfo-py.up.railway.app/api/v1/certificates?search=Abu
    This performs a query by all the above mentioned fields



The list can be sorted by date or ID either in ascending or descending order

    e.g

    Ascending 
    https://certinfo-py.up.railway.app/api/v1/certificates?ordering=id
    

    Descending
    https://certinfo-py.up.railway.app/api/v1/certificates?ordering=-id




## 2. Local setup
 - Clone the repository

    __git clone https://github.com/iAmKabiru/certinfo_py.git__

 - Install dependencies 

    __pip install -r requirements.txt__

 - Run the application

    __python manage.py runserver__

 - Access it in browser by going to __127.0.0.1:8000__
    


## Screenshots of Swagger UI

You can use to try the api

![Screenshot 2023-01-01 112634](https://user-images.githubusercontent.com/26511181/210167659-1eb4f03c-1a70-443c-8eed-d59cd30371d7.png)


![Screenshot 2023-01-01 112921](https://user-images.githubusercontent.com/26511181/210167677-9ad62b7b-f76b-40c6-b1cc-c863fd9ceb91.png)
