# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 11:18:41 2023

@author: robma
"""

portion_down_payment = 0.25
current_savings = 0
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semiannual raise, as a decimal:"))

number_of_months = 0
while total_cost * portion_down_payment > current_savings:
    current_savings += (annual_salary/12) *portion_saved
    investment = current_savings*0.04/12
    current_savings += investment
    number_of_months += 1
    if number_of_months % 6 == 0:
        annual_salary += annual_salary*semi_annual_raise


print("Number of month:", number_of_months)