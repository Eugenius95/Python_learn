class TemperatureConverter:
    def __init__(self, celsius):
        """Constructor to initialize the temperature in Celsius."""
        self.__celsius = celsius

    def set_temperature(self, celsius):
        """Setter method to update the temperature."""
        self.__celsius = celsius

    def get_temperature(self):
        """Getter method to retrieve the temperature in Celsius."""
        return self.__celsius

# Outside the class
# Create an instance with an initial temperature of 25.0
temp_converter = TemperatureConverter(25.0)

# Update the temperature to 30.0
temp_converter.set_temperature(30.0)

# Print the current temperature
print("Current Temperature in Celsius:", temp_converter.get_temperature())
