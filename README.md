# currerter
Simple currency converter.

# Usage

1. Download the repo
```shell
git clone https://github.com/rustbas/currerter.git
```

2. Create the database
```shell
cd app/currerter_app/sqlite3/
cat create_tables.sql | sqlite database.sqlite3
```

3. Migrate the databases
```shell
cd app
./manage migrate
```

4. Run the server
```shell
cd app
./manage runserver
```
