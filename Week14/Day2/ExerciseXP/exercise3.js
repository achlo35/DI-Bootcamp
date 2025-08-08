// Exercise 3 : The temperature converter
// Instructions
// Store a celsius temperature into a variable.

// Convert it to fahrenheit and console.log <temperature>°C is <temperature>°F.
// Hint : Should you create another variable to hold the temperature in fahrenheit? (ie. point 2)
// Hint: To convert a temperature from celsius to fahrenheit : Divide it by 5, then multiply it by 9, then add 32

let celsiusTemperature = 25;
let fahrenheitTemperature = (celsiusTemperature / 5 * 9) + 32;
console.log(`${celsiusTemperature}°C is ${fahrenheitTemperature}°F`);