# Quick Technical Test
### Use
This is a basic CRUD service project with PostgreSQL, for the manipulation of basic users taking into account processes such as authentication and transactional processes.

## Designed by:
Daissi Bibiana Gonzalez Roldan
**E-Mail:** dbgroldan@gmail.com

### How to use this project

1. **Clone this Repo**
  ```sh
  → git clone
  ```
2. **Build the Dockerfile**
  ```sh
  → docker-compose build
  ```

3. **If there were no errors in the previous step**
  ```sh
  → docker-compose up
  ```

4. **Enter the web page, on the routes:**

[127.0.0.1:4000](http://127.0.0.1:3000 "Link a Pagina")

[localhost:4000](http://localhost:3000/ "Link a Pagina")

### Documentation
Here you will find the documentation of all end points:
[Postman: Documentation](https://documenter.getpostman.com/view/10068931/T1LPE7Ee "Link a Pagina")

### Test Mode
To start the testing process completely, you can run the command:
```sh
→ pytest -v
```

If you want to run the tests located within a certain script, you can run the command:
```sh
→ pytest src/tests/script_name.py
```

### Recommendations
* Recuerda que como usuario predeterminado puedes ingresar con los siguientes datos:
```json
{
    "email": "user@example.com",
    "password": "secure"
}
```

* Si desea hacer la instalacion del proyecto con una configuracion distinta, recuerde modificar las variables de entorno en su archivo **.env**,  siguiendo el ejemplo representado en **.env.example**

### License
MIT License
