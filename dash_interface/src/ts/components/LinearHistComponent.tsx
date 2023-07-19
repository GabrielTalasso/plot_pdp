import React, { useEffect, useRef } from "react";
import { DashComponentProps } from "../props";
import { linearhist } from "../graphs/linearhist";

type Props = {
  histData: Array<any>;
  x_axis: string;
  y_axis: string;
  histValue: string;
  value?: string;
} & DashComponentProps;

/**
 * Component description
 */
const LinearHistComponent: React.FC<Props> = ({
  id,
  data,
  histData,
  setProps,
  x_axis,
  y_axis,
  histValue,
  value = "",
}) => {
  const element = useRef();
  function setValue(newValue: string) {
    setProps({ value: newValue });
  }

  useEffect(() => {
    console.log(histValue);
    linearhist(
      data,
      histData,
      element.current,
      x_axis,
      y_axis,
      histValue,
      setValue
    );
  });

  return (
    <div id={id} ref={element}>
      <input
        value={value}
        onChange={(e) => setProps({ value: e.target.value })}
      />
    </div>
  );
};

LinearHistComponent.defaultProps = {};

export default LinearHistComponent;
