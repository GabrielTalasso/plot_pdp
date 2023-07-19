# AUTO GENERATED FILE - DO NOT EDIT

#' @export
histogramplotComponent <- function(children=NULL, id=NULL, data=NULL, value=NULL, xEnd=NULL, xStart=NULL) {
    
    props <- list(children=children, id=id, data=data, value=value, xEnd=xEnd, xStart=xStart)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'HistogramplotComponent',
        namespace = 'my_dash_components',
        propNames = c('children', 'id', 'data', 'value', 'xEnd', 'xStart'),
        package = 'myDashComponents'
        )

    structure(component, class = c('dash_component', 'list'))
}
