import ast 
def extract_list_from_string(input_string):
    result = ast.literal_eval(input_string) # Safely evaluate the string as a Python literal
    if isinstance(result,list):
        return result
    else:            
        return None
# Example usage
input_string = "[1, 2, 3, 4, 5]"
extracted_list = extract_list_from_string(input_string)
if extracted_list is not None:
    print(extracted_list)  # Output: [1, 2, 3, 4, 5]
else:    
    print("The input string does not contain a valid list.")