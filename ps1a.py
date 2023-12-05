# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 11:59:46 2023

@author: robma
"""

portion_down_payment = 0.25
current_savings = 0
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))


number_of_months = 0
while current_savings < total_cost * portion_down_payment:
    current_savings += (annual_salary/12) *portion_saved
    investment = current_savings*0.04/12
    current_savings += investment
    number_of_months += 1
    print("current savings: ", current_savings, "month: ", number_of_months)

print("Number of month:", number_of_months)
