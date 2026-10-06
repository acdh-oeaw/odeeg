#!/bin/bash

pg_dump -d odeeg -h localhost -p 5433 -U  odeeg -c -f odeeg_dump.sql
psql -U postgres -d odeeg < odeeg_dump.sql
