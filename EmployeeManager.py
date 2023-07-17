#!/usr/bin/env python
# encoding: utf-8

import json
from flask import request, jsonify, make_response
class EmployeeManager:
    @staticmethod        
    def getEmployeeDetails(name):
        with open('data.txt', 'r') as fileData:
            data = fileData.read()
            records = json.loads(data)
            for record in records:
                if record["name"] == str(name):
                    return jsonify(record)
            return make_response("employee not found", 404)
        
    @staticmethod   
    def getEmployees():
        with open('data.txt', 'r') as fileData:
            data = fileData.read()
            records = json.loads(data)
            return records
    
    @staticmethod   
    def getEmployeesByGender(gender):
        genderedRecord = []
        with open('data.txt', 'r') as fileData:
            data = fileData.read()
            records = json.loads(data)
            for r in records:
                if r["gender"] == str(gender):
                 genderedRecord.append(r)
        return genderedRecord

    @staticmethod   
    def getEmployeesByDesignation(designation):
        genderedRecord = []
        with open('data.txt', 'r') as fileData:
            data = fileData.read()
            records = json.loads(data)
            for r in records:
                if r["designation"] == str(designation):
                 genderedRecord.append(r)
        return genderedRecord
    
    @staticmethod   
    def getEmployeesOlderThan(age):
        olderRecord = []
        with open('data.txt', 'r') as fileData:
            data = fileData.read()
            records = json.loads(data)
            for r in records:
                if(r["age"] > age):
                    olderRecord.append(r)
        return olderRecord
        
    @staticmethod   
    def addEmployee():
        record = json.loads(request.data)
        with open('data.txt', 'r') as fileData:
            data = fileData.read()
        if not data:
            records = [record]
        else:
            records = json.loads(data)
            records.append(record)
        with open('data.txt', 'w') as fileData:
            fileData.write(json.dumps(records, indent=2))
        return make_response("success", 200)
    
    @staticmethod
    def editEmployee(name):
        record = json.loads(request.data)
        new_records = []
        exists = 0
        with open('data.txt', 'r') as fileData:
            data = fileData.read()
            records = json.loads(data)
        for r in records:
            if r["name"] == name:
                record = r
                exists = 1
            new_records.append(r)
        with open('data.txt', 'w') as fileData:
            fileData.write(json.dumps(new_records, indent=2))
        if(exists == 0):
            return make_response("employee not found", 404)
        return make_response("success", 200)
    
    @staticmethod
    def deleteEmployee(name):
        exists = 0
        new_records = []
        with open('data.txt', 'r') as fileData:
            data = fileData.read()
            records = json.loads(data)
            for r in records:
                if r["name"] == name:
                    exists = 1
                    continue
                new_records.append(r)
        with open('data.txt', 'w') as fileData:
            fileData.write(json.dumps(new_records, indent=2))
        if(exists == 0): 
            return make_response("employee not found", 404)
    
        return make_response("success", 200)
        