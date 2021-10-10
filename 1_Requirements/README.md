# Requirements:
## Introduction:
This project, programmed in python, will fetch the data of an employee from the ecxel sheets when searched by their PS number.

## Features:
💨**Speed**

🟢**Opensource**



## Objective:
- To design a robust tool that will extract employee's data fast from an excel sheet when needed.
- Testing using Pytest
- Write the code using user-defined functions
- No usage of libraries such as pandas, Numpy, etc.

## SWOT Analysis:
### Strength:

1.Can read the file without any errors.

2.Easy to access.

3.No redundancy will be found.

4.An execel sheet can store thousands of data.

### Weakness:
1. Data duplication can cause problems.

### Oppurtinities:
1. Opportunity to make the program deal data duplicity well.

### Threats:
1. Possibility to encapsulate the data.
2. Data Duplicity.
3. It is hard to protect the confidential data.



## 4W's and 1H:
### WHAT:.  
1. It shows percitular persons data from all excel sheets with only the ID number.
2. It generates a new excel sheet for the output data.

### WHERE:
1. To access the data of office employees.
2. College/School students information.
3. Any organisation data regarding work.
4. Accountants use for regualar basis.
### WHEN:
1. It shows particular persons data from all excel sheets with only the PS number.
2. To filter or to access data of one student frorm many excel sheets.

### WHO:
1. Any person from perticular organisation with valid access.
2. Program can be used in both small scale and large scale companies to read and reteieve data.

### HOW:
Infromation with a common ID is beign stored or saved in many excel sheets. At the time to know ones perticular data, can access by giving Id number as input.
So can get whole information of person in a new excel sheet.


## Functional Requirements:
### High Level Requirements:

|*HLR.NO|Description|Status(implemented/ future)*|
|-------|------|------|
|HLR_1| The excel sheet should have 5 sheets with 15 rows and 20 columns| Implemented|
|HLR_2| The excel sheet should be with random data| Implemented|
|HLR_3| All sheets should have one primary data - PS Number| Implemented|
|HLR_4| The system must allow users to view and search in the excel sheets| Implemented|
|HLR_5| Not using the inbuilt fuctions of python| Implemented|
|HLR_6| The program should have only user-defined functions| Implemented|
|HLR_7| The program should not be using the inbuilt fuctions of python| Implemented|

### Low Level Requirements:
|*LLR.No|Description|Dependency*|
|------|-------|----------|
|LLR-1| The user should be able to find list of 15 ps numbers |HLR-1,2,3,4,5,6,7|
|LLR-2| If searched for a correct ps number the releated data must be accessable |HLR-1,2,3,4,5,6,7|
|LLR-3| The output generated must be a new excel sheet with searched data |HLR-1,2,3,4,5,6,7|
|LLR-4| The new excel sheet must be available in the same directory of original excel sheets |HLR-1,2,3,4,5,6,7|


## NON-FUNCTIONAL REQUIREMENTS:
1. The system should be Smooth, user friendly and must be secured.
2. The system must be reliable.
3. The system should be portable, hence supportable.
4. The system should be easy to maintain.
5. The sheets must be accessable.
6. There should be no redundency
## Gantt Chart:
![chart](https://user-images.githubusercontent.com/89696284/136698012-716fe787-869a-4ea1-8d00-6c8c96fc4cba.PNG)
