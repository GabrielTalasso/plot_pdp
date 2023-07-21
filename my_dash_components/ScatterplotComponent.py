# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class ScatterplotComponent(Component):
    """A ScatterplotComponent component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional)

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- data (list of boolean | number | string | dict | lists; required):
    Update props to trigger callbacks."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'my_dash_components'
    _type = 'ScatterplotComponent'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, data=Component.REQUIRED, **kwargs):
        self._prop_names = ['children', 'id', 'data']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'data']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['data']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(ScatterplotComponent, self).__init__(children=children, **args)
