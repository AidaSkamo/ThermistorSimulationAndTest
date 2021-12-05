from ThermistorSimulation import ThermistorSimulation


def simulation_function():
    path = "ntcg163jf103ft1.csv"
    return ThermistorSimulation(path)


def test_verify_source_voltage_value():
    source_voltage = 5.3
    voltage_div = 1.3
    simulate = simulation_function()
    assert simulate.simulate(source_voltage, voltage_div) is None


def test_verify_voltage_divider_value():
    source_voltage = 3.3
    voltage_div = 5
    simulate = simulation_function()
    assert simulate.simulate(source_voltage, voltage_div) is None


def test_verify_output_temperature1():
    source_voltage = 3.3
    voltage_div = 3.106338028
    simulate = simulation_function()
    assert round(simulate.simulate(source_voltage, voltage_div), 2) == -37


def test_verify_output_temperature2():
    source_voltage = 2.97
    voltage_div = 1.42970335
    simulate = simulation_function()
    assert round(simulate.simulate(source_voltage, voltage_div), 2) == 27


def test_verify_output_temperature3():
    source_voltage = 3.63
    voltage_div = 0.605
    simulate = simulation_function()
    assert round(simulate.simulate(source_voltage, voltage_div), 2) == 73.67

