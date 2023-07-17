#!/usr/bin/env python
# encoding: utf-8

from flask import Flask
from EmployeeManager import *

EmployeeManager = EmployeeManager()

app = Flask(__name__)
@app.route('/Employees/<name>', methods=['GET'])
def getEmployeeDetails(name):
    return EmployeeManager.getEmployeeDetails(name)

@app.route('/Employees', methods = ['GET'])
def getEmployees():
    return EmployeeManager.getEmployees()

@app.route('/Employees/Gender/<gender>', methods=['GET'])
def getEmployeesByGender(gender):
    return EmployeeManager.getEmployeesByGender(gender)

@app.route('/Employees/Designation/<designation>', methods=['GET'])
def getEmployeesByDesignation(designation):
    return EmployeeManager.getEmployeesByDesignation(designation)

@app.route('/Employees/Age/<age>', methods=['GET'])
def getEmployeesOlderThan(age):
    return EmployeeManager.getEmployeesOlderThan(age)

@app.route('/Employees', methods=['POST'])
def addEmployee():
    return EmployeeManager.addEmployee()

@app.route('/Employees/<name>', methods=['PUT'])
def editEmployee(name):
    return EmployeeManager.editEmployee(name)

@app.route('/Employees/<name>', methods=['DELETE'])
def deleteEmployee(name):
    return EmployeeManager.deleteEmployee(name)


app.run()