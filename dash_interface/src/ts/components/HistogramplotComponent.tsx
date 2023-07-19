import React, { useEffect, useRef } from "react";
import { DashComponentProps } from "../props";
import { histogramplot } from "../graphs/histogramplot";

type Props = {
  value: string;
  xStart?: Number;
  xEnd?: Number;
} & DashComponentProps;

/**
 * Component description
 */
const HistogramplotComponent: React.FC<Props> = ({
  id,
  data,
  value,
  xStart,
  xEnd,
}) => {
  const element = useRef();

  useEffect(() => {
    histogramplot(data, element.current, value, xStart, xEnd);
  });

  return <div id={id} ref={element}></div>;
};

HistogramplotComponent.defaultProps = {};

export default HistogramplotComponent;
