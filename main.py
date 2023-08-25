def main():
    """
    ##################################################
    # Comlete your code here
    Use the same variables: celcius fahrenheit 
    ##################################################
    """
    celsius= int(input("Enter the temparature in Celsius: "))
    print(celsius)
    fahrenheit= (float(celsius) * 1.8) +32
    print (format (fahrenheit, ".2f"))
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return celsius, fahrenheit


if __name__ == '__main__':
    main()
