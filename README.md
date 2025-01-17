# Ninja savsh | Documentation
It's an api made in Django Ninja, to be used on future project.

## Api's features
- CRUD for expenses and metas.

## Requirements
- Docker

## Build and run container
```
docker-compose up --build
```
```
docker-compose up
```
__This message shows container it's running__

<img src="pics/Captura de ecrã 2025-01-17 181009.png" style="width: 500px"> 

## Content-type: application/json __expense__
```bash
{
  "name": "string",
  "value": "string",
  "validity": "string",
  "amount": 0
}
```

## Content-type: application/json __meta__
```bash
{
  "value": "string",
  "description": "string"
}
```

``` application is running on http://localhost:8000/docs```