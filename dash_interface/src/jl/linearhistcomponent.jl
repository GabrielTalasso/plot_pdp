# AUTO GENERATED FILE - DO NOT EDIT

export linearhistcomponent

"""
    linearhistcomponent(;kwargs...)
    linearhistcomponent(children::Any;kwargs...)
    linearhistcomponent(children_maker::Function;kwargs...)


A LinearHistComponent component.

Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional)
- `id` (String; optional): Unique ID to identify this component in Dash callbacks.
- `data` (Array of Bool | Real | String | Dict | Arrays; required): Update props to trigger callbacks.
- `histData` (Array of Bool | Real | String | Dict | Arrays; required)
- `histValue` (String; required)
- `value` (String; optional)
- `x_axis` (String; required)
- `y_axis` (String; required)
"""
function linearhistcomponent(; kwargs...)
        available_props = Symbol[:children, :id, :data, :histData, :histValue, :value, :x_axis, :y_axis]
        wild_props = Symbol[]
        return Component("linearhistcomponent", "LinearHistComponent", "my_dash_components", available_props, wild_props; kwargs...)
end

linearhistcomponent(children::Any; kwargs...) = linearhistcomponent(;kwargs..., children = children)
linearhistcomponent(children_maker::Function; kwargs...) = linearhistcomponent(children_maker(); kwargs...)

