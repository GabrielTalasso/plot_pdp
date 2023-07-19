# AUTO GENERATED FILE - DO NOT EDIT

export scatterplotcomponent

"""
    scatterplotcomponent(;kwargs...)
    scatterplotcomponent(children::Any;kwargs...)
    scatterplotcomponent(children_maker::Function;kwargs...)


A ScatterplotComponent component.

Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional)
- `id` (String; optional): Unique ID to identify this component in Dash callbacks.
- `data` (Array of Bool | Real | String | Dict | Arrays; required): Update props to trigger callbacks.
"""
function scatterplotcomponent(; kwargs...)
        available_props = Symbol[:children, :id, :data]
        wild_props = Symbol[]
        return Component("scatterplotcomponent", "ScatterplotComponent", "my_dash_components", available_props, wild_props; kwargs...)
end

scatterplotcomponent(children::Any; kwargs...) = scatterplotcomponent(;kwargs..., children = children)
scatterplotcomponent(children_maker::Function; kwargs...) = scatterplotcomponent(children_maker(); kwargs...)

