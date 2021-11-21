# Certi

This application is made for the challenge made by certi on the technical interview.

**candidate =>** Juan Gabriel Sousa Andrade

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
```bash
curl http://127.0.0.1:5000/
```