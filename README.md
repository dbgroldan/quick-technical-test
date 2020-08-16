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

2. **If there were no errors in the previous step**
  ```sh
  → docker-compose up
  ```

3. **Enter the web page, on the routes:**

[127.0.0.1:80](http://127.0.0.1 "Link a Pagina")

[localhost:80](http://localhost "Link a Pagina")

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
*  If you want to install the project with a different configuration, remember to modify the environment variables in your **.env** file, following the example represented in  **.env.example**

* In the same way, if you want to manually configure your database, initially you can execute the following commands in your *PostgreSQL* database, remembering to do the modification of the respective environment variables in the same way:
~~~~sql
CREATE DATABASE db_name;
CREATE USER user_name with ENCRYPTED PASSWORD 'paswword';
GRANT ALL PRIVILEGES ON database db_name TO user_name;
~~~~

### License
MIT License
