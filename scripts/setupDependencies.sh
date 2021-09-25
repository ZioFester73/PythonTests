#!/bin/bash

# https://egkatzioura.com/2020/10/19/run-a-docker-postgresql-instance-locally-for-testing/

#-d Run container in background and print container ID
#--rm Automatically remove the container when it exists

docker container stop $(docker container ls -aq)

sleep 2

docker run -d --rm --name test-instance -p 5432:5432 -e POSTGRES_PASSWORD=abcd1234 postgres

set -e

export PGPASSWORD=abcd1234;

sleep 2

psql -v ON_ERROR_STOP=1 -h localhost -p 5432 -U postgres <<-EOSQL
    create schema test_schema;

    create table test_schema.employee(
        id  SERIAL PRIMARY KEY,
        firstname   TEXT    NOT NULL,
        lastname    TEXT    NOT NULL,
        email       TEXT    not null,
        age         INT     NOT NULL,
        salary         real,
        unique(email)
    );

    insert into test_schema.employee (firstname,lastname,email,age,salary)
    values ('John','Doe 1','john1@doe.com',18,1234.23);

EOSQL

