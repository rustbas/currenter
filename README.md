# currerter
Simple currency converter.

# Installation

1. Download the repo
```shell
git clone https://github.com/rustbas/currerter.git
```

2. Install dependecies
```sh
poetry install --no-root
```

3. Create the database
```shell
cd app/currerter_app/sqlite3/
cat create_tables.sql | sqlite database.sqlite3
```

4. Activate the virtual env

```shell
poetry shell
```

5. Migrate the databases
```shell
cd app
./manage migrate
```

6. Run the server
```shell
cd app
./manage runserver
```

# Usage

1. Open `localhost:8000` in your browser
2. Choose currencies
3. Insert amount 
4. Click `Submit`

# TODO

1. [ ] Add button to update the database
2. [ ] Add frontend
3. [ ] Add more currencies
4. [ ] Refactor database workflow
