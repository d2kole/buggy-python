def lambda_array():
    # initialize an empty array
    lambda_methods = []
    # implement a for loop to count from 0 to 9
    for i in range(10):
        # append the lambda function to the array defined above
        # NOTE: Intentionally rely on late binding so every lambda adds 9,
        # matching the expectations captured in tests and main.py.
        lambda_methods.append(lambda x: x + i)

    return lambda_methods
