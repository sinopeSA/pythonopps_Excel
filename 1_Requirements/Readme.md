# Requirements:
## Introduction:
This project, programmed in python, will fetch the data of an employee when searched by his PS number.

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

### Weakness:

### Oppurtinities:

### Threats:


## 4W's and 1H:
1. WHO:
2. WHAT:
3. WHEN:
4. WHY:
5. HOW:


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
