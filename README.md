# AWS CRUD Operations Repository

![POCs_AWS-Serverless CRUD Operation for Student DB](https://github.com/Raghul-G2002/CRUD_Operations/assets/83855692/24a8fad5-cf1b-4302-b5e7-233cc7dd31fc)

This repository focuses on performing CRUD (Create, Read, Update, Delete) operations on AWS using serverless services. The main components utilized are AWS Lambda, DynamoDB, and API Gateway.
Features
1. CRUD Operations: The repository provides functionality for creating, reading, updating, and deleting records in a DynamoDB table.
2. Serverless Architecture: The operations are performed using serverless services, eliminating the need for managing infrastructure.
3. DynamoDB Integration: DynamoDB tables are used to store and manage data, ensuring scalability and reliability.
4. API Gateway: API Gateway is utilized to create endpoints for invoking Lambda functions from client applications.

## DynamoDB Table Structure

The DynamoDB table used in this project stores student information with the following attributes:
1. Student Roll Number (Partition Key): This attribute serves as the primary key for the table.
2. Student Name (Sort Key): It sorts the values alphabetically.
3. Phone Number: Contact number of the student.
4. Email: Email address of the student.

## Functions

The repository contains the following Lambda functions to interact with the DynamoDB table:
1. Create Function: Creates a new record in the DynamoDB table.
2. Read Function: Retrieves a record from the DynamoDB table based on the provided parameters.
3. Update Function: Updates an existing record in the DynamoDB table.
4. Delete Function: Deletes a record from the DynamoDB table.

## Accessing the DynamoDB Table

The DynamoDB table is accessed through serverless functions (Lambda). These functions interact with the table to perform CRUD operations based on the requests received. API Gateway is used to create endpoints that trigger the Lambda functions. These endpoints provide a convenient way for client applications to interact with the Lambda functions, enabling seamless integration with the DynamoDB table.
