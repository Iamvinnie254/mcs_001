# gauss-Jacobi method for solving system of linear equations

# initial approximations

x = 0
y = 0
z = 0

# number of iterations
n = 20

for i in range(1, n + 1):
    x_new = (12 - 2 * y - z) / 5
    y_new = (15 - x - 2 * z) / 4
    z_new = (20 - x - 2 * y) / 5

    # this line displays the iteration results
    print(f"{i:<12}{x_new:<15.2f}{y_new:<15.2f}{z_new:<15.2f}")

    x, y, z = x_new, y_new, z_new


print("Final approximations:")
print(f"x = {x:.2f}")
print(f"y = {y:.2f}")
print(f"z = {z:.2f}")

"""

Results:

1           2.40           3.75           4.00           
2           0.10           1.15           2.02           
3           1.54           2.71           3.52           
4           0.61           1.61           2.61           
5           1.24           2.29           3.24           
6           0.84           1.82           2.84           
7           1.10           2.12           3.10           
8           0.93           1.92           2.93           
9           1.05           2.05           3.05           
10          0.97           1.97           2.97           
11          1.02           2.02           3.02           
12          0.99           1.99           2.99           
13          1.01           2.01           3.01           
14          0.99           1.99           2.99           
15          1.00           2.00           3.00           
16          1.00           2.00           3.00           
17          1.00           2.00           3.00           
18          1.00           2.00           3.00           
19          1.00           2.00           3.00           
20          1.00           2.00           3.00           
Final approximations:
x = 1.00
y = 2.00
z = 3.00

"""
