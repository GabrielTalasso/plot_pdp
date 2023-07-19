import React, { useEffect, useRef } from "react";
import { DashComponentProps } from "../props";
import { scatterplot } from "../graphs/scatterplot";

type Props = {
  // Insert props
} & DashComponentProps;

/**
 * Component description
 */
const ScatterplotComponent:React.FC<Props> = ({id, data}) => {
  const element = useRef();

  useEffect(() => {
    scatterplot(data, element.current);
  });

  return <div id={id} ref={element}></div>;
};

ScatterplotComponent.defaultProps = {};

export default ScatterplotComponent;
