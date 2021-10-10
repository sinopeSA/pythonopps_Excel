## TEST PLAN:

## High level test plan

| **Test ID** | **Description**                   | **Exp I/P**| **Exp O/P** | **Actual Out** |    
|-------------|-----------------------------------|------------|-------------|----------------|
|  H_01       | PS number                         | Search PS number  |  Valid/Invalid | SUCCESS |
|  H_02       | Employee PS number                | Data request |Obtained data        | SUCCESS |
|  H_03       | New excel sheet with requested data| PS number | New file generated    | SUCCESS |

## Low Level test plan

| **Test ID**| **HL_ID** | **Description** | **Exp I/P** | **Exp O/P** | **Actual Out** | **Pass/Fail** |
| --------- | ---- |----------------------- | ----------- | ----------- | -------------- | --------------|
|  L_01     | H_01 | PS number               | PS number            | Valid/Invalid  |   SUCCESS  | PASS |
|  L_02     | H_02 | Information request     | PS number and Data   | Requested data |   SUCCESS  | PASS |
|  L_03     | H_02 | Employee marks data     | PS number and Data   |  Employee marks|   SUCCESS  | PASS |
|  L_04     | H_02 | Employee travel data    | PS number and Data   |  Travel data   |   SUCCESS  | PASS |
|  L_05     | H_02 | Employee Programing skills|  PS number and Data | Programing skills|   SUCCESS  | PASS |
|  L_06     | H_02 | Employee Domain          | PS number and Data  | Domain information|  SUCCESS  | PASS |
|  L_07     | H_03 | New Excel sheet          | PS number           | Excel sheet with expected data |  SUCCESS | PASS |
 


