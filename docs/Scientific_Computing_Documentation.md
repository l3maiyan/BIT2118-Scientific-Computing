# BIT 2118: SCIENTIFIC COMPUTING
## Individual Practical Work and Documentation

**Student name:** [Enter your full name]  
**Registration number:** [Enter your registration number]  
**Course:** [Enter course/programme]  
**Unit:** BIT 2118 – Scientific Computing  
**Lecturer:** [Enter lecturer's name]  
**Submission date:** [Enter date]  
**GitHub repository URL:** [Paste your individual GitHub URL here]

---

## 1. Introduction

Scientific computing uses computers, numerical methods and mathematical models to solve problems that may be difficult or time-consuming to solve by hand. This practical work uses Python together with NumPy, SciPy and Matplotlib. NumPy is used for arrays, matrix calculations and numerical operations. SciPy provides numerical algorithms such as root finding, interpolation, integration and optimization. Matplotlib is used to display graphs.

The work follows the supplied BIT 2118 brief. Each task identifies its inputs and mathematical operation, changes at least one input or parameter, explains the effect, and applies the method to a different but related real-world situation.

## 2. Software and libraries

- **Python:** programming language used to implement the numerical methods.
- **NumPy:** arrays, vectorized calculations, matrix algebra and numerical operations.
- **SciPy:** LU decomposition, numerical root finding, interpolation, curve fitting, integration, differential-equation solving and optimization.
- **Matplotlib:** graphs used to display data, fitted curves and numerical convergence.

Install the required libraries with `python -m pip install -r requirements.txt`.

---

## 3. Task documentation

### Task 2 – NumPy Arrays and Numerical Computation

**Concept:** A NumPy array stores numerical values in an organized structure. NumPy can calculate statistics and apply formulas to all array elements.

**Original problem:** A weather station records hourly temperatures. The program calculates the mean, minimum and maximum temperature and converts readings from Celsius to Fahrenheit.

**Inputs:** 24 temperature readings in degrees Celsius, stored in `temperatures_c`.

**Operations:** `np.mean()`, `np.min()`, `np.max()` and the conversion formula \(F=1.8C+32\).

**Output and meaning:** The mean represents the average daily temperature. The minimum and maximum show the coldest and hottest readings. Fahrenheit values are the same measurements expressed in another unit.

**Changed input:** The program adds 2°C to every reading. The new mean also increases by 2°C, while the minimum and maximum each increase by 2°C.

**Related real-world case:** Aquarium water-temperature monitoring. A new array stores water readings and calculates the average and whether all readings remain within the assumed 24–26°C range.

**Assumption:** The readings are valid measurements taken at regular hourly intervals.

### Task 3 – Mathematical Functions and Vectorization

**Concept:** Vectorization applies one mathematical operation to an entire array without writing a Python loop for every value.

**Original problem:** Convert one million simulated network-latency readings from milliseconds to seconds and square them.

**Inputs:** One million random latency values between 5 and 250 milliseconds. A fixed random seed makes the generated data repeatable.

**Operations:** Divide each value by 1000 and square it. The program compares a Python-loop implementation with a NumPy vectorized implementation using `timeit`.

**Output and meaning:** The first five values show the transformed measurements. The timing comparison shows how long each approach takes on the computer running the program. Actual timing can vary by computer.

**Changed input:** The program uses 100,000 readings instead of one million. Fewer values require less total computation.

**Related real-world case:** Convert sensor distance readings from centimetres to metres using one vectorized expression.

**Assumption:** Latency readings are non-negative and the generated sample is representative for demonstrating the method.

### Task 4 – Floating-Point Arithmetic and Numerical Errors

**Concept:** Computers store many decimal fractions as binary approximations. This can cause small rounding differences.

**Original problem:** Compare `0.1 + 0.2` with `0.3`.

**Inputs:** Decimal values 0.1, 0.2 and 0.3.

**Operations:** Addition, exact equality comparison, absolute error and NumPy's `isclose()` tolerance comparison.

**Output and meaning:** The exact comparison may be false because the stored binary values are not perfectly exact. The tolerance comparison treats sufficiently small differences as equal.

**Changed parameter:** The program explicitly uses an absolute tolerance of \(10^{-8}\). A tolerance defines the maximum difference accepted as close enough.

**Related real-world case:** Check whether a sensor measurement of 12.50000001 is sufficiently close to a reference value of 12.5 using a tolerance of \(10^{-6}\).

**Assumption:** The tolerance is selected based on the precision required by the measurement system.

### Task 5 – Matrix Algebra and Matrix Operations

**Concept:** A matrix is a rectangular arrangement of values. Matrix multiplication can represent transformations such as rotation and scaling.

**Original problem:** Rotate three two-dimensional points by 90 degrees.

**Inputs:** A 3-by-2 array of point coordinates and a 2-by-2 rotation matrix.

**Operations:** Matrix multiplication using `@` and the transpose of the transformation matrix.

**Output and meaning:** The transformed coordinates show the new positions of the points after rotation.

**Changed parameter:** The 90-degree rotation matrix is replaced by a 180-degree rotation matrix. The points move to the opposite direction around the origin.

**Related real-world case:** Scale diagram or graphics coordinates by a factor of two.

**Assumption:** The points are two-dimensional and transformations are performed around the origin.

### Task 6 – Solution of Systems of Linear Equations

**Concept:** A system of simultaneous linear equations can be written as \(Ax=b\). NumPy solves for the unknown vector \(x\).

**Original problem:** Estimate the number of two server types from total CPU and memory usage.

**Inputs:** Coefficient matrix `A` containing resource usage per server type and vector `b` containing total CPU and memory usage.

**Operations:** `np.linalg.solve(A, b)` solves the simultaneous equations. Matrix multiplication checks the solution.

**Output and meaning:** The solution gives the estimated number of Type A and Type B servers. The residual should be close to zero if the solution satisfies the equations.

**Changed input:** Total CPU usage is increased from 20 to 24 units while memory remains 72 GB. The estimated server combination changes to satisfy the new totals.

**Related real-world case:** Determine quantities of two ingredients needed to meet protein and energy targets by solving two simultaneous equations.

**Assumption:** Resource usage is additive and the coefficient matrix has a unique solution.

### Task 7 – Gaussian Elimination and LU Decomposition

**Concept:** Gaussian elimination removes unknowns to solve a linear system. LU decomposition factors a matrix into lower- and upper-triangular matrices so the factorization can be reused.

**Original problem:** Solve several measurement systems that share the same coefficient matrix.

**Inputs:** A 3-by-3 coefficient matrix and three right-hand-side measurement vectors.

**Operations:** `lu_factor()` factors the matrix once; `lu_solve()` uses the factorization for each measurement vector. Residual norms check accuracy.

**Output and meaning:** Each solution estimates the unknown values for one measurement set. Small residual norms indicate that the equations are satisfied closely.

**Changed input:** The first value of the first measurement vector changes from 15 to 18. The resulting solution changes because the right-hand side has changed.

**Related real-world case:** Repeated water-flow balance estimates in a pipe network using the same network coefficient matrix.

**Assumption:** The coefficient matrix is nonsingular and the same network structure is used for each measurement set.

### Task 8 – Iterative Methods for Linear Systems

**Concept:** Jacobi and Gauss-Seidel methods improve an initial estimate repeatedly until the change becomes smaller than a tolerance.

**Original problem:** Estimate steady-state temperatures at five interior points between two fixed temperature boundaries.

**Inputs:** Matrix `A`, boundary vector `b`, initial guess of zero, tolerance and maximum iteration count.

**Operations:** Jacobi updates all values using the previous iteration. Gauss-Seidel uses newly calculated values immediately. The infinity norm measures the largest change.

**Output and graph meaning:** The printed vectors are the estimated temperatures. The convergence graph shows the maximum change per iteration. A decreasing curve indicates that the estimates are settling toward a solution.

**Changed input:** The left boundary influence is increased from 100 to 120. The estimated interior temperatures change because the boundary condition has changed.

**Related real-world case:** Model temperatures in five connected rooms with different boundary temperatures.

**Assumption:** The chosen system is diagonally dominant so the iterative methods converge for this demonstration.

### Task 9 – Eigenvalues and Eigenvectors

**Concept:** An eigenvector of a square matrix keeps its direction under a matrix transformation. Its eigenvalue describes the scaling factor.

**Original problem:** Estimate the relative importance of nodes in a small undirected computer network.

**Inputs:** A 4-by-4 adjacency matrix describing connections among nodes A, B, C and D.

**Operations:** `np.linalg.eig()` calculates eigenvalues and eigenvectors. The eigenvector associated with the largest real eigenvalue is normalized so its scores add to one.

**Output and meaning:** The scores represent relative eigenvector-based network importance. A node connected to important nodes can receive a higher score.

**Changed input:** A new connection is added between nodes A and D. The network matrix and the resulting importance scores change.

**Related real-world case:** Treat the same connection pattern as collaboration links among IT, Finance, HR and Operations departments.

**Assumption:** The network is undirected, and the adjacency matrix uses 1 for a connection and 0 for no connection.

### Task 10 – Root Finding: Bisection and Fixed-Point Methods

**Concept:** Root finding searches for a value where a function equals zero. Bisection repeatedly halves an interval containing a sign change. Fixed-point iteration repeatedly evaluates \(x_{n+1}=g(x_n)\).

**Original problem:** Find an equilibrium temperature using a heat-balance function.

**Inputs:** Heat-balance function, bisection interval [20, 40], initial fixed-point estimate of 30°C and convergence tolerance.

**Operations:** SciPy `root_scalar()` with the bisection method and repeated fixed-point updates.

**Output and meaning:** Both methods estimate the temperature at which the heat-balance function is zero. Similar results provide a useful cross-check.

**Changed parameter:** The constant offset in the heat-balance equation changes from 25 to 27. The equilibrium temperature changes as a result.

**Related real-world case:** Estimate an operating threshold for equipment using a related nonlinear balance equation.

**Assumption:** The selected bisection interval contains a root and the fixed-point iteration converges from the chosen starting value.

### Task 11 – Root Finding: Newton-Raphson and Secant Methods

**Concept:** Newton-Raphson uses a derivative to improve a root estimate. The secant method estimates the derivative using two nearby points.

**Original problem:** Find the internal rate of return (IRR) of an investment by finding the discount rate that makes net present value (NPV) equal to zero.

**Inputs:** Initial investment of -10,000 and annual cash inflows of 3,000, 3,500, 4,000 and 2,500.

**Operations:** The program defines NPV and its derivative, then applies SciPy's Newton and secant root-finding methods.

**Output and meaning:** The IRR is the estimated discount rate that makes NPV approximately zero. The NPV check verifies the root.

**Changed input:** The initial investment increases from 10,000 to 11,000. The investment requires a different break-even return, so the estimated IRR changes.

**Related real-world case:** Calculate the break-even discount rate for purchasing equipment with a different set of cash flows.

**Assumption:** Cash flows occur at equal yearly intervals and the selected starting values allow the numerical solver to converge.

### Task 12 – Polynomial and Nonlinear Equation Solving

**Concept:** Nonlinear systems contain equations that are not all linear in their unknowns. Numerical solvers search for values that make all residuals close to zero.

**Original problem:** Find intersection points of a circle and a parabola.

**Inputs:** Circle equation \(x^2+y^2=4\), parabola equation \(y=x^2-1\), and initial guesses.

**Operations:** The `root()` function from SciPy solves the two residual equations.

**Output and meaning:** The returned x and y values estimate an intersection. Small residuals show that the point satisfies both equations closely.

**Changed parameter:** The circle radius increases from 2 to 2.5. The intersection location changes.

**Related real-world case:** Find an operating point where two nonlinear production constraints meet.

**Assumption:** The initial guess is sufficiently close to an intersection for the numerical solver to converge.

### Task 13 – Interpolation

**Concept:** Interpolation estimates values between known data points. Linear interpolation joins neighboring points with straight lines; cubic splines use smooth cubic curves.

**Original problem:** Estimate temperatures at ten-minute intervals from hourly sensor readings.

**Inputs:** Hour values from 8:00 to 14:00 and seven measured temperatures.

**Operations:** SciPy `interp1d()` creates a linear interpolation function; `CubicSpline()` creates a smooth cubic interpolation function.

**Output and graph meaning:** The estimates provide temperatures between measured hours. The graph compares the measured points with the two interpolation curves.

**Changed input:** The 11:00 reading changes from 24°C to 26°C. Estimates near that point change because the interpolation uses the supplied measurements.

**Related real-world case:** Estimate water level at hour 3 from readings taken every two hours.

**Assumption:** Measurements are ordered by time and interpolation is used between the first and last measured times, not for long-range extrapolation.

### Task 14 – Curve Fitting and Approximation

**Concept:** Curve fitting finds model parameters that make a mathematical curve follow observed data. The program uses least-squares fitting.

**Original problem:** Model server response time as the number of concurrent users increases.

**Inputs:** Seven user-load measurements and their observed response times in milliseconds.

**Operations:** `curve_fit()` estimates the parameters of a quadratic model \(y=ax^2+bx+c\). RMSE measures the typical size of prediction errors.

**Output and graph meaning:** The fitted equation describes the observed trend. The graph compares measured points with the fitted curve. The prediction at 400 users is an estimate, not a guaranteed measurement.

**Changed input:** 20 ms is added to each observed response time. The fitted model's predicted response times increase.

**Related real-world case:** Fit a quadratic model to machine energy use at different production levels.

**Assumption:** A quadratic curve is a reasonable approximation over the range being studied. Predictions outside the measured range should be treated cautiously.

### Task 15 – Numerical Differentiation

**Concept:** A derivative measures the rate at which a quantity changes. Numerical differentiation estimates it from nearby measurements.

**Original problem:** Estimate vehicle speed from GPS position readings.

**Inputs:** Time values in seconds and position values in metres.

**Operations:** Forward difference is used at the first point, central differences at interior points, and backward difference at the final point.

**Output and graph meaning:** The calculated values estimate speed in metres per second. The graph shows how estimated speed changes over time.

**Changed input:** The position reading at 3 seconds changes from 16.1 m to 17.1 m. Speed estimates around that time are affected.

**Related real-world case:** Estimate water flow rate from cumulative water-volume readings.

**Assumption:** Time values are increasing and measurements are sufficiently close together for finite differences to be useful.

### Task 16 – Numerical Integration

**Concept:** Integration estimates accumulated quantity or the area under a curve. The trapezoidal rule uses trapezoids, while Simpson's rule uses parabolic approximations.

**Original problem:** Estimate energy use from smart-meter power readings.

**Inputs:** Power readings in kilowatts at two-hour intervals.

**Operations:** NumPy's trapezoidal integration and SciPy's `simpson()` integrate power over time.

**Output and meaning:** The result is estimated energy in kilowatt-hours (kWh). The difference between the two methods shows how their approximations compare for the same readings.

**Changed input:** All power readings increase by 10%. The estimated energy also increases by 10% because integration is linear in the measured power values.

**Related real-world case:** Estimate the total volume of water delivered from flow-rate readings over 30 minutes.

**Assumption:** Readings represent the power or flow rate between the listed time points, and time units are used consistently.

### Task 17 – Ordinary Differential Equations: Euler Method

**Concept:** An ordinary differential equation describes how a value changes with time. Euler's method estimates the next value using the current rate of change and a chosen step size.

**Original problem:** Model the cooling of a hot object using Newton's law of cooling.

**Inputs:** Ambient temperature 25°C, initial temperature 90°C, cooling constant 0.12 per minute, one-minute step size and 30-minute duration.

**Operations:** Apply \(T_{n+1}=T_n+h[-k(T_n-T_{ambient})]\) at each time step. The exact solution is also calculated for comparison.

**Output and graph meaning:** The final Euler temperature is compared with the exact temperature. The graph shows the numerical approximation and exact cooling curve.

**Changed parameter:** Step size is reduced from 1 minute to 0.5 minute. A smaller step generally improves Euler accuracy but requires more calculations.

**Related real-world case:** Estimate population growth using the simple model \(dP/dt=rP\).

**Assumption:** The cooling constant and ambient temperature remain constant throughout the simulation.

### Task 18 – Numerical Solution of ODEs Using SciPy

**Concept:** SciPy's `solve_ivp()` solves an initial-value differential equation using numerical methods and adaptive step sizes.

**Original problem:** Model voltage in a charging RC circuit.

**Inputs:** Supply voltage 5 V, resistance 1,000 ohms, capacitance 0.001 farads, initial voltage 0 V and time interval from 0 to 5 seconds.

**Operations:** Solve \(dV/dt=(V_s-V)/(RC)\) with `solve_ivp()`. Compare the numerical solution with the exact RC charging formula.

**Output and graph meaning:** The output reports solver success, voltage at 5 seconds and maximum error. The graph compares numerical and exact voltage curves.

**Changed parameter:** Resistance increases to 2,000 ohms. The circuit charges more slowly, so its voltage after five seconds is lower.

**Related real-world case:** Model first-order decay of a substance from an initial amount of 100 units.

**Assumption:** Circuit components are ideal and resistance and capacitance remain constant.

### Task 19 – Numerical Optimization

**Concept:** Optimization finds values that minimize or maximize an objective function while satisfying constraints.

**Original problem:** Minimize server operating cost while providing at least 1,000 units of processing capacity.

**Inputs:** Type A cost 12 and capacity 100; Type B cost 18 and capacity 170; minimum capacity 1,000; non-negative decision variables.

**Operations:** SciPy `minimize()` with the SLSQP method minimizes the cost function subject to the capacity inequality and non-negative bounds.

**Output and meaning:** The allocation values show the recommended quantities in the continuous model. The total capacity should meet or exceed the requirement, and the objective value is the estimated minimum cost.

**Changed parameter:** Required capacity increases from 1,000 to 1,200. The optimized allocation and minimum cost change to satisfy the higher requirement.

**Related real-world case:** Minimize delivery costs while meeting a required carrying capacity using two vehicle types.

**Assumption:** The model permits fractional allocation units. If actual servers or vehicles must be whole units, integer constraints or a separate integer search are needed.

### Task 20 – Random Numbers and Monte Carlo Methods

**Concept:** Monte Carlo methods use repeated random sampling to estimate probabilities or other quantities.

**Original problem:** Estimate the probability that incoming server demand exceeds server capacity.

**Inputs:** Capacity 1,000, normally distributed demand with mean 850 and standard deviation 120, and 100,000 simulations.

**Operations:** NumPy generates random demand values. A Boolean condition checks whether demand exceeds capacity. The mean of the Boolean results estimates the overload probability.

**Output and graph meaning:** The estimated probability is the proportion of simulated cases that exceed capacity. The running-probability graph shows how the estimate changes as more simulations are included. It should generally become more stable as the sample size increases.

**Changed parameter:** Mean demand increases from 850 to 900 while capacity and standard deviation remain the same. The overload probability is expected to increase.

**Related real-world case:** Estimate the probability that daily customer arrivals exceed a service capacity of 220 customers.

**Assumption:** Demand follows a normal distribution and simulations are independent. The random seed makes the demonstration repeatable.

---

## 4. General conclusion

The tasks demonstrate how Python libraries can be used to solve different numerical problems. NumPy makes array and matrix operations easier, while SciPy provides tools for solving equations, estimating unknown values, integrating data, solving differential equations and optimizing resources. Matplotlib makes numerical results easier to understand through graphs.

Changing inputs and parameters is important because it shows how sensitive a model is to different conditions. The related real-world examples also demonstrate that the same mathematical method can be adapted to different practical problems.

## 5. References

1. BIT 2118 Scientific Computing Group Work brief supplied for this assignment.
2. NumPy documentation: https://numpy.org/doc/
3. SciPy documentation: https://docs.scipy.org/doc/scipy/
4. Matplotlib documentation: https://matplotlib.org/stable/

---

**Student reminder:** Replace all bracketed student details, run the scripts, inspect the actual outputs and graphs, and ensure you can explain the work before submitting.
