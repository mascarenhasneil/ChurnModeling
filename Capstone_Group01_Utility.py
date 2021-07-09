"""
Final Capstone Project. Group 1
ALY6140 80956 Analytics Systems Technology SEC 04 Spring 2021 CPS

Title: Customer Churn Modeling.

Copyright (c) 2021
Licensed
Written by Neil Mascarenhas
Date: 10 May 2021
"""



def Test():   # Not required but a good practice to check if this file is accessible 
    print("Capstone Test Successful")


def EstimatedSalary_FE(bcd):
    bcd.loc[bcd['EstimatedSalary'] <= 40007, 'EstimatedSalary'] = 0
    bcd.loc[(bcd['EstimatedSalary'] > 40007) & (bcd['EstimatedSalary'] <= 80003), 'EstimatedSalary'] = 1
    bcd.loc[(bcd['EstimatedSalary'] > 80003) & (bcd['EstimatedSalary'] <= 120000), 'EstimatedSalary'] = 2
    bcd.loc[(bcd['EstimatedSalary'] > 120000) & (bcd['EstimatedSalary'] <= 159996), 'EstimatedSalary'] = 3
    bcd.loc[bcd['EstimatedSalary'] > 159996, 'EstimatedSalary'] = 4

    return bcd

def Balance_FE(bcd):
    bcd.loc[bcd['Balance'] <= 0, 'Balance'] = 0
    bcd.loc[(bcd['Balance'] > 0) & (bcd['Balance'] <= 251), 'Balance'] = 1
    bcd.loc[(bcd['Balance'] > 251) & (bcd['Balance'] <= 50179), 'Balance'] = 2
    bcd.loc[(bcd['Balance'] > 50179) & (bcd['Balance'] <= 100359), 'Balance'] = 3
    bcd.loc[(bcd['Balance'] > 100359) & (bcd['Balance'] <= 150538), 'Balance'] = 4
    bcd.loc[(bcd['Balance'] > 150538) & (bcd['Balance'] <= 200718), 'Balance'] = 5
    bcd.loc[(bcd['Balance'] > 200718) & (bcd['Balance'] <= 250000), 'Balance'] = 6
    return bcd

def CreditScore_FE(bcd):
    bcd.loc[bcd['CreditScore'] <= 450, 'CreditScore'] = 0
    bcd.loc[(bcd['CreditScore'] > 450) & (bcd['CreditScore'] <= 550), 'CreditScore'] = 1
    bcd.loc[(bcd['CreditScore'] > 550) & (bcd['CreditScore'] <= 650), 'CreditScore'] = 2
    bcd.loc[(bcd['CreditScore'] > 650) & (bcd['CreditScore'] <= 750), 'CreditScore'] = 3
    bcd.loc[(bcd['CreditScore'] > 750) & (bcd['CreditScore'] <= 850), 'CreditScore'] = 4
    bcd.loc[(bcd['CreditScore'] > 850), 'CreditScore'] = 5
    return bcd
