# AUTO GENERATED FILE - DO NOT EDIT

export histogramplotcomponent

"""
    histogramplotcomponent(;kwargs...)
    histogramplotcomponent(children::Any;kwargs...)
    histogramplotcomponent(children_maker::Function;kwargs...)


A HistogramplotComponent component.

Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional)
- `id` (String; optional): Unique ID to identify this component in Dash callbacks.
- `data` (Array of Bool | Real | String | Dict | Arrays; required): Update props to trigger callbacks.
- `value` (String; required)
- `xEnd` (optional): . xEnd has the following type: lists containing elements 'toString', 'toFixed', 'toExponential', 'toPrecision', 'valueOf', 'toLocaleString'.
Those elements have the following types:
  - `toString` (optional): Returns a string representation of an object.
@,param,radix, ,Specifies a radix for converting numeric values to strings. This value is only used for numbers.
  - `toFixed` (required): Returns a string representing a number in fixed-point notation.
@,param,fractionDigits, ,Number of digits after the decimal point. Must be in the range 0 - 20, inclusive.
  - `toExponential` (required): Returns a string containing a number represented in exponential notation.
@,param,fractionDigits, ,Number of digits after the decimal point. Must be in the range 0 - 20, inclusive.
  - `toPrecision` (required): Returns a string containing a number represented either in exponential or fixed-point notation with a specified number of digits.
@,param,precision, ,Number of significant digits. Must be in the range 1 - 21, inclusive.
  - `valueOf` (optional): Returns the primitive value of the specified object.
  - `toLocaleString` (optional): Converts a number to a string by using the current or specified locale.
@,param,locales, ,A locale string or array of locale strings that contain one or more language or locale tags. If you include more than one locale string, list them in descending order of priority so that the first entry is the preferred locale. If you omit this parameter, the default locale of the JavaScript runtime is used.
@,param,options, ,An object that contains one or more properties that specify comparison options.
@,param,locales, ,A locale string, array of locale strings, Intl.Locale object, or array of Intl.Locale objects that contain one or more language or locale tags. If you include more than one locale string, list them in descending order of priority so that the first entry is the preferred locale. If you omit this parameter, the default locale of the JavaScript runtime is used.
@,param,options, ,An object that contains one or more properties that specify comparison options.. toLocaleString has the following type: lists containing elements .
Those elements have the following types:

- `xStart` (optional): . xStart has the following type: lists containing elements 'toString', 'toFixed', 'toExponential', 'toPrecision', 'valueOf', 'toLocaleString'.
Those elements have the following types:
  - `toString` (optional): Returns a string representation of an object.
@,param,radix, ,Specifies a radix for converting numeric values to strings. This value is only used for numbers.
  - `toFixed` (required): Returns a string representing a number in fixed-point notation.
@,param,fractionDigits, ,Number of digits after the decimal point. Must be in the range 0 - 20, inclusive.
  - `toExponential` (required): Returns a string containing a number represented in exponential notation.
@,param,fractionDigits, ,Number of digits after the decimal point. Must be in the range 0 - 20, inclusive.
  - `toPrecision` (required): Returns a string containing a number represented either in exponential or fixed-point notation with a specified number of digits.
@,param,precision, ,Number of significant digits. Must be in the range 1 - 21, inclusive.
  - `valueOf` (optional): Returns the primitive value of the specified object.
  - `toLocaleString` (optional): Converts a number to a string by using the current or specified locale.
@,param,locales, ,A locale string or array of locale strings that contain one or more language or locale tags. If you include more than one locale string, list them in descending order of priority so that the first entry is the preferred locale. If you omit this parameter, the default locale of the JavaScript runtime is used.
@,param,options, ,An object that contains one or more properties that specify comparison options.
@,param,locales, ,A locale string, array of locale strings, Intl.Locale object, or array of Intl.Locale objects that contain one or more language or locale tags. If you include more than one locale string, list them in descending order of priority so that the first entry is the preferred locale. If you omit this parameter, the default locale of the JavaScript runtime is used.
@,param,options, ,An object that contains one or more properties that specify comparison options.. toLocaleString has the following type: lists containing elements .
Those elements have the following types:

"""
function histogramplotcomponent(; kwargs...)
        available_props = Symbol[:children, :id, :data, :value, :xEnd, :xStart]
        wild_props = Symbol[]
        return Component("histogramplotcomponent", "HistogramplotComponent", "my_dash_components", available_props, wild_props; kwargs...)
end

histogramplotcomponent(children::Any; kwargs...) = histogramplotcomponent(;kwargs..., children = children)
histogramplotcomponent(children_maker::Function; kwargs...) = histogramplotcomponent(children_maker(); kwargs...)

