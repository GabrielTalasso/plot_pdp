# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class LinearHistComponent(Component):
    """A LinearHistComponent component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional)

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- data (list of boolean | number | string | dict | lists; required):
    Update props to trigger callbacks.

- histData (list of boolean | number | string | dict | lists; required)

- histValue (string; required)

- value (string; optional)

- x_axis (string; required)

- y_axis (string; required)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'my_dash_components'
    _type = 'LinearHistComponent'
    @_explicitize_args
    def __init__(self, children=None, histData=Component.REQUIRED, x_axis=Component.REQUIRED, y_axis=Component.REQUIRED, histValue=Component.REQUIRED, value=Component.UNDEFINED, id=Component.UNDEFINED, data=Component.REQUIRED, **kwargs):
        self._prop_names = ['children', 'id', 'data', 'histData', 'histValue', 'value', 'x_axis', 'y_axis']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'data', 'histData', 'histValue', 'value', 'x_axis', 'y_axis']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['data', 'histData', 'histValue', 'x_axis', 'y_axis']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(LinearHistComponent, self).__init__(children=children, **args)
