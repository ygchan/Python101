# Overview of workflow

# ---------------------------------------------
# Introduction of Data Ingestion with Python
# ---------------------------------------------

# 1. Acquire data
# 2. Clean data
# 3. Train Model 
# 4. Evaluate Model
# 5. Need more data
# 6. Need more data

# Source of data are from database, log files
# API provide data from logs

# Python can easily ingest data from various of sources

# Type of data: 
# records (from relational data)
# metrics (mixed of int/float in HDF5)
# graphs  (neo4j)
# textual (plain text file)

# Data Pipeline (ETL)
# Most of them are from server log files 
# Take them into database is ETL

# Extract Transform and Load
# ETL Tasks: convert 2020-01-01 to datetime(2020, 1, 1)
# Validate: 2020-02-30 > error
# Enrich: Using IP and convert to location
# Missing Data handle

# Clean Data (Data Lake)
# Put them into one data source
# The program all hit this one final place

# Spark - computation plaform
# Get familiar with the data lakes.

# Q: Why do we prefer to work with data lakes?
# It's a single source for all data.

# Q: Data validation is a part of the data pipeline
# YES!

# Q: What is NOT a type of data?
# API

# Q: Where does data come from?
# Database (????)

# Q: Data scientists spend the majority of their time acquiring and cleaning data.
# True

# ---------------------------------------------
# Chapter 02: Reading Data
# ---------------------------------------------

# CSV: 
# Pro: Easy export/import from excel
# Cons: No type information, No Standard

# Process text file become a bottle neck
# Parquet, Avro, ORC.

# Find a library and load them into Pandas.
# Use Apache Arrow

# Use regular expression, please put the sample in source code.
# Practice regular expression to parse log.
# Import it into dataware house.











