## TEST PLAN:

## High level test plan

| **Test ID** | **Description**                   | **InPut**| **Output** | **Status** |    
|-------------|-----------------------------------|------------|-------------|----------------|
|  H_01       | PS number                         | Search PS number  |  Valid/Invalid | Implemented |
|  H_02       | Employee PS number                | Data request |Obtained data        | Implemented |
|  H_03       | New excel sheet with requested data| PS number | New file generated    | Implemented |

## Low Level test plan

| **Test ID**| **HL_ID** | **Description** | **InPut** | **OutPut** | **Status** | **Pass/Fail** |
| --------- | ---- |----------------------- | ----------- | ----------- | -------------- | --------------|
|  L_01     | H_01 | PS number               | PS number            | Valid/Invalid  |   Implemented  | PASS |
|  L_02     | H_02 | Information request     | PS number and Data   | Requested data |   Implemented  | PASS |
|  L_03     | H_02 | Employee marks data     | PS number and Data   |  Employee marks|   Implemented  | PASS |
|  L_04     | H_02 | Employee travel data    | PS number and Data   |  Travel data   |   Implemented  | PASS |
|  L_05     | H_02 | Employee Programing skills|  PS number and Data | Programing skills| Implemented | PASS |
|  L_06     | H_02 | Employee Domain          | PS number and Data  | Domain information|  Implemented | PASS |
|  L_07     | H_03 | New Excel sheet       | PS number  | Excel sheet with expected data | Implemented | PASS |
 


