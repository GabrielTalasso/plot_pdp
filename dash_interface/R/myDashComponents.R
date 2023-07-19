# AUTO GENERATED FILE - DO NOT EDIT

#' @export
myDashComponents <- function(children=NULL, id=NULL, data=NULL) {
    
    props <- list(children=children, id=id, data=data)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'MyDashComponents',
        namespace = 'my_dash_components',
        propNames = c('children', 'id', 'data'),
        package = 'myDashComponents'
        )

    structure(component, class = c('dash_component', 'list'))
}
