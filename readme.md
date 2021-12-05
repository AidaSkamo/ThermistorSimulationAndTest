Thermistor simulation and unit tests 

Two provided python scripts contain simulation and 5 unit tests.
To run the tests, execute `pytest -v ` from the terminal. Make sure you are executing the command from correct folder.

`thermistor_test.py` script contains `simulation_function()`, object of class ThermistorSimulation is created.
Filepath (name of the csv file containing characteristic) is hardcoded in a script. Make sure file used when testing has the same name.

Default source_voltage value as well as the allowed error are provided as 
hardcoded values - attributes of the `ThermistorSumulation` class.

Parsing of the csv file is done, ignoring the first 6 rows in the csv file, loading values of temperature and nominal ntc resistance into a variable of type dictionary.
Conversion form degrees C to K is not done as it was not necessary [(x-y) degC == (x-y) K]. Since all resistance values are given in kOhms the conversion is to Ohms is done during reading of the csv file into a variable of type dictionary.

`simulate()` function requires input arguments be validated.  `def calculate_min_divider_voltage(self, v_s):` and `def calculate_max_divider_voltage(self, v_s):` are used to calculate max and min voltage that can be measured at the divider point for the provided resistor values in the csv.

Linear interpolation function is implemented so that two adjacent values, one that is bigger and one that is smaller than the calculated value of resistance of the thermistor.
Using rearranged expression for linear interpolation [(y-y0)/(x-x0)]=[(y1-y0)/(x1-x0)]
