#!/bin/bash

cd /path/to/wp/install

wp db export /tmp/backup.sql

wp core update
wp theme update --all
wp plugin update --all
