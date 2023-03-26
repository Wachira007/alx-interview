#!/usr/bin/python3
def pascal_triangle(n):

    """Pascal Challenge"""
    # Check if n is less than or equal to 0, and return an empty list if so
    if n <= 0:
        return []
    
    # Create an empty list to hold the Pascal's triangle
    triangle = [[1]]
    
    # Iterate over each row of the triangle (starting from the second row)
    for i in range(1, n):
        # Create a new list to hold the current row of the triangle
        row = [1]
        
        # Iterate over each element in the middle of the row
        for j in range(1, i):
            # Calculate the sum of the corresponding elements in the previous row,
            # and add this value to the current row
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        
        # Add the last element (which is always 1) to the current row
        row.append(1)
        
        # Add the current row to the triangle
        triangle.append(row)
    
    # Return the completed triangle
    return triangle
