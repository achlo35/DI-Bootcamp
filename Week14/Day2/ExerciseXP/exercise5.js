// Exercise 5 : Guess the answers #2
// Instructions
// For each expression, in a Javascript file in VS CODE, predict what you think the output will be in a comment (//) without first running the command.
// Of course, explain each prediction.

// Then run the expression in the console of your browser (NOT IN VS CODE).

// Note the actual output in a comment and compare it with your prediction.

typeof(15)
// Prediction: number, because 15 is a numeric value
// Actual: number

typeof(5.5)
// Prediction: number, because 5.5 is a float number
// Actual: number

typeof(NaN)
// Prediction: number, because NaN stands for "Not a Number" but is still considered a numeric type in JavaScript
// Actual: number

typeof("hello")
// Prediction: string, because "hello" is a sequence of characters enclosed in quotes
// Actual: string

typeof(true)
// Prediction: boolean, because true is a boolean value
// Actual: boolean

typeof(1 != 2)
// Prediction: boolean, because 1 is not equal to 2, which results in a boolean value
// Actual: boolean

"hamburger" + "s"
// Prediction: hamburgers, because we are concatenating two strings
// Actual: "hamburgers"

"hamburgers" - "s"
// Prediction: NaN, because we cannot subtract a string from another string
// Actual: NaN

"1" + "3"
// Prediction: 13, because we are concatenating two strings
// Actual: 13

"1" - "3"
// Prediction: NaN, because we cannot subtract two strings
// Actual: NaN

"johnny" + 5
// Prediction: "johnny5", because we are concatenating a string with a number
// Actual: "johnny5"

"johnny" - 5
// Prediction: NaN, because we cannot subtract a number from a string
// Actual: NaN

99 * "hello"
// Prediction: NaN, because we cannot multiply a number by a string
// Actual: NaN

1 != 1
// Prediction: false, because 1 is equal to 1
// Actual: false

1 == "1"
// Prediction: false because a number cannot be equal to a string, even if they represent the same value.
// Actual: true

1 === "1"
// Prediction: false, because strict equality checks both value and type, and a number is not equal to a string
// Actual: false