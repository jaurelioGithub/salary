# salary.py

def salary(hours, hourly_wage):
    """Calculates the salary considering the number of hours and the hourly wage.
    
    Exaple:
        >>> salary(30,2000)
        
        (60000)

    Args:
        hours(int): number of hours
        hourly_wage(int): hourly wage

    Returns:
        (int):total salary       
    """    
    if hours<=40:
        return hours*hourly_wage
    else:
        return 40*hourly_wage+(hours-40)*hourly_wage*1.5

def main():
    print(salary(30,2000))

if __name__ == "__main__":
    main()
