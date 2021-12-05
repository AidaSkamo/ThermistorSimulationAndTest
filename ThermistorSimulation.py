import csv
import os.path


class ThermistorSimulation:
    default_source_voltage = 3300e-3
    default_error_value_positive = 0.1
    default_error_value_negative = -0.1
    r = 10000
    list_of_keys = []
    list_of_values = []
    _ntc_char = {}

    def __init__(self, filepath):
        self.filepath = filepath
        # verify file exist in provided location
        if not os.path.exists(filepath):
            print("File does not exist or the provided path is incorrect! Provide correct path!")
        else:
            with open(filepath) as csv_file:
                for index, row in enumerate(csv.reader(csv_file)):
                    if index > 5:
                        for index_col, i in enumerate(row):
                            if index_col == 0:
                                self.list_of_keys.append(float(i))
                            elif index_col == 2:
                                self.list_of_values.append(float(i)*1000)
        self._ntc_char = dict(zip(self.list_of_keys, self.list_of_values))
        if len(self._ntc_char) == 0:
            print("File is empty! Provide a different path.")

    def calculate_min_divider_voltage(self, v_s):
        r_min = self._ntc_char[min(self._ntc_char, key=self._ntc_char.get)]
        v_min = v_s*r_min/(r_min + self.r)
        return v_min

    def calculate_max_divider_voltage(self, v_s):
        r_max = self._ntc_char[max(self._ntc_char, key=self._ntc_char.get)]
        v_max = v_s*r_max/(r_max + self.r)
        return v_max

    def linear_interpolation(self, thermistor_resistance):
        # find number smaller and number greater than provided resistance
        y_0 = self._ntc_char[min(self._ntc_char, key=self._ntc_char.get)]
        y_1 = self._ntc_char[max(self._ntc_char, key=self._ntc_char.get)]
        for i in self._ntc_char:
            if thermistor_resistance >= self._ntc_char[i] >= y_0:
                y_0 = self._ntc_char[i]
                x_0 = i
        for i in self._ntc_char:
            if y_1 >= self._ntc_char[i] >= thermistor_resistance:
                y_1 = self._ntc_char[i]
                x_1 = i

        temperature = (thermistor_resistance - y_0)*(x_1-x_0)/(y_1-y_0) + x_0
        return temperature

    def simulate(self, voltage_s, voltage_div):
        # validate inputs for reference value +- 10%
        if voltage_s < self.default_source_voltage * (1 + self.default_error_value_negative) or voltage_s > self.default_source_voltage * (1 + self.default_error_value_positive):
            print("Source voltage value out of boundaries! Provide value within boundaries!")
            return None
        elif voltage_div < self.calculate_min_divider_voltage(voltage_s) or voltage_div > self.calculate_max_divider_voltage(voltage_s):
            print("Voltage value at the divider point is out of boundaries! Provide value within boundaries!")
            return None

        # calculate the value of ntc resistance for the provided value of voltage at the divider point
        r_ntc = (voltage_div * self.r) / (voltage_s - voltage_div)
        temper = self.linear_interpolation(r_ntc)
        return temper





