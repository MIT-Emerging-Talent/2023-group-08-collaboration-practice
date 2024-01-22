def add_string_numbers(num1, num2):
    """ A function that adds two string numbers. 
    
        Input
        -----
        num1 : a string number (int, float, double convertible only)
        num2 : a string number (int, float, double convertible only) 
        
        Output
        ------
        result_str : a string """
    
    # check the input strings are convertible to numeric
    try:
        # convert the input strings to numeric types
        num1 = float(num1)
        num2 = float(num2)

        # add the numbers
        result = num1 + num2

        # convert the result back to a string and remove trailing zeros for floats
        result_str = "{:.10f}".format(result).rstrip('0').rstrip('.')

        return result_str
    
    # catch the exception
    except ValueError:
        # handle the case where input strings are not valid numbers
        raise ValueError("Invalid input: Please provide valid numeric strings")