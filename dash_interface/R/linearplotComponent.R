# AUTO GENERATED FILE - DO NOT EDIT

#' @export
linearplotComponent <- function(children=NULL, id=NULL, data=NULL, value=NULL, xEnd=NULL, xStart=NULL, x_axis=NULL, y_axis=NULL) {
    
    props <- list(children=children, id=id, data=data, value=value, xEnd=xEnd, xStart=xStart, x_axis=x_axis, y_axis=y_axis)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'LinearplotComponent',
        namespace = 'my_dash_components',
        propNames = c('children', 'id', 'data', 'value', 'xEnd', 'xStart', 'x_axis', 'y_axis'),
        package = 'myDashComponents'
        )

    structure(component, class = c('dash_component', 'list'))
}
