# Employee Salary Calculation Program

This repository aims to provide a comprehensive starting point for understanding and implementing an employee salary calculation system. This program is implemented in Python and is suitable as an introduction to employee data management and salary calculation, which is appropriate for beginner and intermediate programmers. In this repository, you will find examples of how to record employee data, calculate salaries based on working hours, allowances, and deductions, and generate salary reports.

<hr><br>

## Purpose of This Repository

This repository aims to provide a complete guide to understanding and implementing an employee salary calculation system. This program is implemented in Python and is designed to help companies accurately and efficiently calculate employee salaries. In this repository, you will find examples of how to record employee data, calculate salaries based on working hours, allowances, and deductions, and generate monthly salary reports. This program is very suitable for beginner and intermediate programmers who want to learn practical applications in human resource management.

<hr><br>

## Demonstration

Here is a demonstration of the main function from the program:

```python
def calculate_salary(hours_worked, hourly_rate, allowances, deductions):
    gross_salary = hours_worked * hourly_rate
    net_salary = gross_salary + allowances - deductions
    return net_salary

# Example usage
hours_worked = 160
hourly_rate = 20
allowances = 300
deductions = 50

net_salary = calculate_salary(hours_worked, hourly_rate, allowances, deductions)
print(f"Net Salary: ${net_salary}")
```

<hr><br>

## Features

- Record employee data
- Calculate salaries based on working hours
- Calculate allowances and deductions
- Generate monthly salary reports

<hr><br>

## Technologies Used

- Python
- Pandas (for data management)
- Matplotlib (for data visualization)

<hr><br>

## Project Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/guanshiyin28/Program-Perhitungan-Gaji-Karyawan.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Program-Perhitungan-Gaji-Karyawan
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

<hr><br>

## Steps to Run

1. Run the program:
   ```bash
   python program_v2.py
   python program.py
   ```

<hr><br>

## License

This project is licensed under the Apache-2.0 License. See the [LICENSE](LICENSE) file for details.

<hr><br>

<div align="center">
   <a href="https://www.instagram.com/guanshiyin_/">
      <img src="https://capsule-render.vercel.app/api?type=waving&height=200&color=100:393E46,20:F7F7F7&section=footer&reversal=false&textBg=false&fontAlignY=50&descAlign=48&descAlignY=59"/>
   </a>
</div>
