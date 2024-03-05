#ABCiD API
## Ayrton's Breast Cancer Identificador API
### Exposing API to talk to LUNA's feature

This is just view part, backend will be resposible for sending the details of the image to LUNA and based on that information
she'll predict whether the person has a breast cancer.

Use frontend project as well to a better view 
https://github.com/AyrtonSM/abc-id-front-end

How to run: 

`$ docker build -t breast-cancer-api .` 

`$ docker run --name breast-cancer-api -d -p 5000:5000 breast-cancer-api`
