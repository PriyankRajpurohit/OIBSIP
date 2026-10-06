# Task 2 — BMI Calculator

A beginner-friendly Python command-line program that calculates BMI from weight in kilograms and height in metres, then displays the result to two decimal places and its category.

## Requirements

- Python 3.10 or newer
- No third-party packages

## Run

Open a terminal in this folder and run:

python main.py

On Windows, py main.py may be used if the python command is unavailable. Enter q at either prompt to quit. The program asks again if an entry is not numeric, is not finite, or is zero or negative.

## Example

For a weight of 70 kg and a height of 1.75 m:

- BMI: 22.86
- Category: Normal

## Calculation and categories

BMI = weight in kilograms / (height in metres × height in metres)

- Below 18.5: Underweight
- 18.5 to below 25: Normal
- 25 to below 30: Overweight
- 30 or above: Obese

These labels and cutoffs match the Oasis Task List. The cutoffs correspond to the CDC adult BMI bands. BMI is a screening measure, not a diagnosis, and CDC adult categories are intended for adults aged 20 and older: https://www.cdc.gov/bmi/adult-calculator/bmi-categories.html

## Learning notes

- calculate_bmi contains the formula and checks values.
- bmi_category maps the result to the Task List categories.
- read_positive_number converts typed text to a number and retries invalid entries.
- main connects input, calculation, and displayed output.

This is the Beginner-tier command-line version. It does not store personal records or provide medical advice.
