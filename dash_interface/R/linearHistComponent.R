# AUTO GENERATED FILE - DO NOT EDIT

#' @export
linearHistComponent <- function(children=NULL, id=NULL, data=NULL, histData=NULL, histValue=NULL, value=NULL, x_axis=NULL, y_axis=NULL) {
    
    props <- list(children=children, id=id, data=data, histData=histData, histValue=histValue, value=value, x_axis=x_axis, y_axis=y_axis)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'LinearHistComponent',
        namespace = 'my_dash_components',
        propNames = c('children', 'id', 'data', 'histData', 'histValue', 'value', 'x_axis', 'y_axis'),
        package = 'myDashComponents'
        )

    structure(component, class = c('dash_component', 'list'))
}
