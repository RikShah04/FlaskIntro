#!/usr/bin/env python
# encoding: utf-8

from flask import Flask
from EmployeeManager import *

EmployeeManager = EmployeeManager()

app = Flask(__name__)
@app.route('/Employees', methods=['GET'])
def getEmployeeDetails():
    ID =request.args.get('ID')
    return EmployeeManager.getEmployeeDetails(ID)

@app.route('/Employees/All', methods = ['GET'])
def getEmployees():
    return EmployeeManager.getEmployees()

@app.route('/Employees/Gender:', methods=['GET'])
def getEmployeesByGender():
    gender = request.args.get('gender')
    return EmployeeManager.getEmployeesByGender(gender)

@app.route('/Employees/Designation:', methods=['GET'])
def getEmployeesByDesignation():
    designation = request.args.get('designation')
    return EmployeeManager.getEmployeesByDesignation(designation)

@app.route('/Employees/OlderThan:', methods=['GET'])
def getEmployeesOlderThan():
    age = request.args.get('age')
    return EmployeeManager.getEmployeesOlderThan(age)

@app.route('/Employees', methods=['POST'])
def addEmployee():
    return EmployeeManager.addEmployee()

@app.route('/Employees/Edit:', methods=['PUT'])
def editEmployee():
    ID = request.args.get('ID')
    return EmployeeManager.editEmployee(ID)

@app.route('/Employees/Delete:', methods=['DELETE'])
def deleteEmployee():
    ID = request.args.get('ID')
    return EmployeeManager.deleteEmployee(ID)


app.run()