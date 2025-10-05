# salary.py

def salary(hours, hourly_wage):
    """Calculates the salary considering the number of hours and the hourly wage.
    
    Examples:
        >>> salary(30,2000) 
        60000
        
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
    """Main function that invokes salary function.
    """
    try:
        hours=int(input("Ingrese el numero de horas: "))
        wage=int(input("Ingrese el monto por hora: "))
        print(salary(hours,wage))
    except:
            print("Dato incorrecto!!")    

if __name__ == "__main__":
    main()
