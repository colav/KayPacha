<center><img src="https://raw.githubusercontent.com/colav/colav.github.io/master/img/Logo.png"/></center>

# KayPacha
SQL data extraction for Scienti and Colav parners  Oracle databases

# Description
Package extract the data from SQL databases from Oracle Databases from Scienti or Colav parners
Models are defined here, filters etc..

# Installation

## Package
`pip install kaypacha`


# Usage
Oracle DB Colav docker database for scienti have to be already loaded, [take a look here](https://github.com/colav/oracle-docker)

Remember you only can use max 2 threads due a Oracle XE version limitation [more information here](https://docs.oracle.com/en/database/oracle/oracle-database/18/xeinl/licensing-restrictions.html)

Saving the model product for scienti on MongoDB
`
kaypacha_scienti --model_year 2018 --model product --drop_mongodb --max_threads 2
`

Getting a JSon file sample for the model product for scienti (**WARNING**: getting the full DB in a file require a huge amount of RAM, use it with careful.)
`
kaypacha_scienti --model_year 2018 --model product --json prod.json --max_threads 2
`


# TODO
* support for checkpoints
* implement all the main tables for Scienti. 

# License
BSD-3-Clause License 

# Links
http://colav.udea.edu.co/



