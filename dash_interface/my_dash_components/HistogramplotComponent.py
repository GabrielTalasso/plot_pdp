# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class HistogramplotComponent(Component):
    """A HistogramplotComponent component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional)

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- data (list of boolean | number | string | dict | lists; required):
    Update props to trigger callbacks.

- value (string; required)

- xEnd (dict; optional)

    `xEnd` is a dict with keys:

    - toExponential (required):
        Returns a string containing a number represented in
        exponential notation. @,param,fractionDigits, ,Number of
        digits after the decimal point. Must be in the range 0 - 20,
        inclusive.

    - toFixed (required):
        Returns a string representing a number in fixed-point
        notation. @,param,fractionDigits, ,Number of digits after the
        decimal point. Must be in the range 0 - 20, inclusive.

    - toLocaleString (dict; optional):
        Converts a number to a string by using the current or
        specified locale. @,param,locales, ,A locale string or array
        of locale strings that contain one or more language or locale
        tags. If you include more than one locale string, list them in
        descending order of priority so that the first entry is the
        preferred locale. If you omit this parameter, the default
        locale of the JavaScript runtime is used. @,param,options, ,An
        object that contains one or more properties that specify
        comparison options. @,param,locales, ,A locale string, array
        of locale strings, Intl.Locale object, or array of Intl.Locale
        objects that contain one or more language or locale tags. If
        you include more than one locale string, list them in
        descending order of priority so that the first entry is the
        preferred locale. If you omit this parameter, the default
        locale of the JavaScript runtime is used. @,param,options, ,An
        object that contains one or more properties that specify
        comparison options.

        `toLocaleString` is a dict with keys:


    - toPrecision (required):
        Returns a string containing a number represented either in
        exponential or fixed-point notation with a specified number of
        digits. @,param,precision, ,Number of significant digits. Must
        be in the range 1 - 21, inclusive.

    - toString (optional):
        Returns a string representation of an object. @,param,radix,
        ,Specifies a radix for converting numeric values to strings.
        This value is only used for numbers.

    - valueOf (optional):
        Returns the primitive value of the specified object.

- xStart (dict; optional)

    `xStart` is a dict with keys:

    - toExponential (required):
        Returns a string containing a number represented in
        exponential notation. @,param,fractionDigits, ,Number of
        digits after the decimal point. Must be in the range 0 - 20,
        inclusive.

    - toFixed (required):
        Returns a string representing a number in fixed-point
        notation. @,param,fractionDigits, ,Number of digits after the
        decimal point. Must be in the range 0 - 20, inclusive.

    - toLocaleString (dict; optional):
        Converts a number to a string by using the current or
        specified locale. @,param,locales, ,A locale string or array
        of locale strings that contain one or more language or locale
        tags. If you include more than one locale string, list them in
        descending order of priority so that the first entry is the
        preferred locale. If you omit this parameter, the default
        locale of the JavaScript runtime is used. @,param,options, ,An
        object that contains one or more properties that specify
        comparison options. @,param,locales, ,A locale string, array
        of locale strings, Intl.Locale object, or array of Intl.Locale
        objects that contain one or more language or locale tags. If
        you include more than one locale string, list them in
        descending order of priority so that the first entry is the
        preferred locale. If you omit this parameter, the default
        locale of the JavaScript runtime is used. @,param,options, ,An
        object that contains one or more properties that specify
        comparison options.

        `toLocaleString` is a dict with keys:


    - toPrecision (required):
        Returns a string containing a number represented either in
        exponential or fixed-point notation with a specified number of
        digits. @,param,precision, ,Number of significant digits. Must
        be in the range 1 - 21, inclusive.

    - toString (optional):
        Returns a string representation of an object. @,param,radix,
        ,Specifies a radix for converting numeric values to strings.
        This value is only used for numbers.

    - valueOf (optional):
        Returns the primitive value of the specified object."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'my_dash_components'
    _type = 'HistogramplotComponent'
    @_explicitize_args
    def __init__(self, children=None, value=Component.REQUIRED, xStart=Component.UNDEFINED, xEnd=Component.UNDEFINED, id=Component.UNDEFINED, data=Component.REQUIRED, **kwargs):
        self._prop_names = ['children', 'id', 'data', 'value', 'xEnd', 'xStart']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'data', 'value', 'xEnd', 'xStart']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['data', 'value']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(HistogramplotComponent, self).__init__(children=children, **args)
