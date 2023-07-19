import React, { useEffect, useRef } from "react";
import { DashComponentProps } from "../props";
import { linearplot } from "../graphs/linearplot";

type Props = {
  x_axis: string;
  y_axis: string;
  xStart?: Number;
  xEnd?: Number;
  value?: string;
} & DashComponentProps;

/**
 * Component description
 */
const LinearplotComponent: React.FC<Props> = ({
  id,
  data,
  setProps,
  x_axis,
  y_axis,
  xStart,
  xEnd,
  value = "",
}) => {
  const element = useRef();
  function setValue(newValue: string) {
    setProps({ value: newValue });
  }

  useEffect(() => {
    linearplot(data, element.current, x_axis, y_axis, xStart, xEnd, setValue);
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

LinearplotComponent.defaultProps = {};

export default LinearplotComponent;
