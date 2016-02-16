## Docker image for Uplatnica
[Uplatnica](https://github.com/hrvach/uplatnica) generates Croatian payment slips in vector form.

This library was originally created by GitHub user [Hrvach](https://github.com/hrvach), I just created a docker image for it.

## Spinning up the container
Build the image by running:  
`docker build -t uplatnice .`

Run the container by running:  
`docker run -dp 5000:5000 uplatnice`

## API Usage
The server is running on port 5000 we just exposed with an API that has a single endpoint:  
`POST /uplatnica` - takes the request body filled with the payment slip info in JSON and returns a PDF file of the filled slip

A valid request will look something like this:  
```
POST /uplatnica HTTP/1.1
Host: DOCKER_MACHINE_IP:5000
Content-Type: application/json

{"poziv_na_broj_platitelja": "54321-121-1",
"poziv_na_broj_primatelja": "12345-212-2",
"iznos": "12345",
"iban_primatelja": "HR9223600001501426697",
"iban_platitelja": "HR6025000091000000013",
"model_primatelja": "HR01",
"model_platitelja": "HR05",
"sifra_namjene": "OTLC",
"datum_izvrsenja": "10022016",
"valuta_placanja": "HRK",
"hitno": "X",
"ime_i_prezime_platitelja": "Pero Perić",
"ulica_i_broj_platitelja": "Ilica 1",
"postanski_i_grad_platitelja": "10000 Zagreb",
"naziv_primatelja": "Sklonište za nezbrinute životinje",
"ulica_i_broj_primatelja": "Franjčevićeva 43",
"postanski_i_grad_primatelja": "10361 Dumovec",
"opis_placanja": "Novčani prilog za pomoć nezbrinutim životinjama."}
```
