% Auto-generated: do not edit by hand
\name{linearplotComponent}

\alias{linearplotComponent}

\title{LinearplotComponent component}

\description{

}

\usage{
linearplotComponent(children=NULL, id=NULL, data=NULL, value=NULL, xEnd=NULL,
xStart=NULL, x_axis=NULL, y_axis=NULL)
}

\arguments{
\item{children}{A list of or a singular dash component, string or number. }

\item{id}{Character. Unique ID to identify this component in Dash callbacks.}

\item{data}{List of logical | numeric | character | named list | unnamed lists. Update props to trigger callbacks.}

\item{value}{Character. }

\item{xEnd}{Lists containing elements 'tostring', 'tofixed', 'toexponential', 'toprecision', 'valueof', 'tolocalestring'.
those elements have the following types:
  - tostring (optional): returns a string representation of an object.
@,param,radix, ,specifies a radix for converting numeric values to strings. this value is only used for numbers.
  - tofixed (required): returns a string representing a number in fixed-point notation.
@,param,fractiondigits, ,number of digits after the decimal point. must be in the range 0 - 20, inclusive.
  - toexponential (required): returns a string containing a number represented in exponential notation.
@,param,fractiondigits, ,number of digits after the decimal point. must be in the range 0 - 20, inclusive.
  - toprecision (required): returns a string containing a number represented either in exponential or fixed-point notation with a specified number of digits.
@,param,precision, ,number of significant digits. must be in the range 1 - 21, inclusive.
  - valueof (optional): returns the primitive value of the specified object.
  - tolocalestring (optional): converts a number to a string by using the current or specified locale.
@,param,locales, ,a locale string or array of locale strings that contain one or more language or locale tags. if you include more than one locale string, list them in descending order of priority so that the first entry is the preferred locale. if you omit this parameter, the default locale of the javascript runtime is used.
@,param,options, ,an object that contains one or more properties that specify comparison options.
@,param,locales, ,a locale string, array of locale strings, intl.locale object, or array of intl.locale objects that contain one or more language or locale tags. if you include more than one locale string, list them in descending order of priority so that the first entry is the preferred locale. if you omit this parameter, the default locale of the javascript runtime is used.
@,param,options, ,an object that contains one or more properties that specify comparison options.. tolocalestring has the following type: lists containing elements .
those elements have the following types:
. }

\item{xStart}{Lists containing elements 'tostring', 'tofixed', 'toexponential', 'toprecision', 'valueof', 'tolocalestring'.
those elements have the following types:
  - tostring (optional): returns a string representation of an object.
@,param,radix, ,specifies a radix for converting numeric values to strings. this value is only used for numbers.
  - tofixed (required): returns a string representing a number in fixed-point notation.
@,param,fractiondigits, ,number of digits after the decimal point. must be in the range 0 - 20, inclusive.
  - toexponential (required): returns a string containing a number represented in exponential notation.
@,param,fractiondigits, ,number of digits after the decimal point. must be in the range 0 - 20, inclusive.
  - toprecision (required): returns a string containing a number represented either in exponential or fixed-point notation with a specified number of digits.
@,param,precision, ,number of significant digits. must be in the range 1 - 21, inclusive.
  - valueof (optional): returns the primitive value of the specified object.
  - tolocalestring (optional): converts a number to a string by using the current or specified locale.
@,param,locales, ,a locale string or array of locale strings that contain one or more language or locale tags. if you include more than one locale string, list them in descending order of priority so that the first entry is the preferred locale. if you omit this parameter, the default locale of the javascript runtime is used.
@,param,options, ,an object that contains one or more properties that specify comparison options.
@,param,locales, ,a locale string, array of locale strings, intl.locale object, or array of intl.locale objects that contain one or more language or locale tags. if you include more than one locale string, list them in descending order of priority so that the first entry is the preferred locale. if you omit this parameter, the default locale of the javascript runtime is used.
@,param,options, ,an object that contains one or more properties that specify comparison options.. tolocalestring has the following type: lists containing elements .
those elements have the following types:
. }

\item{x_axis}{Character. }

\item{y_axis}{Character. }
}

\value{named list of JSON elements corresponding to React.js properties and their values}

