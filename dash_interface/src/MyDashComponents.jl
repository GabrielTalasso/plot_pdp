
module MyDashComponents
using Dash

const resources_path = realpath(joinpath( @__DIR__, "..", "deps"))
const version = "1.0.0"

include("jl/histogramplotcomponent.jl")
include("jl/linearhistcomponent.jl")
include("jl/linearplotcomponent.jl")
include("jl/scatterplotcomponent.jl")

function __init__()
    DashBase.register_package(
        DashBase.ResourcePkg(
            "my_dash_components",
            resources_path,
            version = version,
            [
                DashBase.Resource(
    relative_package_path = "my_dash_components.js",
    external_url = nothing,
    dynamic = nothing,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "my_dash_components.js.map",
    external_url = nothing,
    dynamic = true,
    async = nothing,
    type = :js
)
            ]
        )

    )
end
end
