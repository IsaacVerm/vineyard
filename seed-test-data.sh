#!/bin/bash
cd sql
mysql -u root -e "source create-db-and-tables.sql"
mysql -u root -e "source insert-test-data.sql"
