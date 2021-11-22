# Certi

This application is made for the challenge made by certi on the technical interview.

First I want to thank you for the opportunity and I hope you like what you will see

**candidate =>** Juan Gabriel Sousa Andrade

**email =>** juangabriel4699@gmail.com

**linkedin =>** [https://www.linkedin.com/in/juan-andrade-888200212/]()

## Installation

1. Clone the repository

```bash
git clone https://github.com/Dosbodoke/certi_challenge.git
```

2. Build docker image
```bash
docker build -t juan_certi .
```

3. Run docker container
```bash
docker run -d -p 5000:5000 juan_certi
```

## Usage
The application can be used with a custom input via HTTP request, where the endpoin is the number that you want to translate.

```bash
curl http://127.0.0.1:5000/<number>
```

## Test
To run unittest you should start the container and run the following command.

```bash
docker exec -it <container_id> /bin/bash
python3 src/test.py
```