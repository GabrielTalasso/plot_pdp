import React, { Component, useEffect, useState } from "react";
import * as d3 from "d3";
// @ts-ignore
import tsvData from "./data.tsv";
import ScatterplotComponent from "../ts/components/ScatterplotComponent";
import LinearplotComponent from "../ts/components/LinearplotComponent";
import HistogramplotComponent from "../ts/components/HistogramplotComponent";
import LinearHistComponent from "../ts/components/LinearHistComponent";

const App = () => {
  // return runScatterplot()
  // return runLinearplot();
  // return runHistogramplot();
  return runLinearHistComponent();
};

const runLinearHistComponent = () => {''
  const data = [
    { x_axis: 2, y_axis: 3 },
    { x_axis: 2.32, y_axis: 3.5 },
    { x_axis: 2.34, y_axis: 3.1 },
    { x_axis: 2.555, y_axis: 3.8 },
    { x_axis: 2.56, y_axis: 4 },
    { x_axis: 2.57, y_axis: 4 },
    { x_axis: 3, y_axis: 4 },
    { x_axis: 4, y_axis: 5 },
    { x_axis: 4, y_axis: 5 },
    { x_axis: 4, y_axis: 5 },
    { x_axis: 4, y_axis: 5 },
    { x_axis: 4, y_axis: 5 },
    { x_axis: 4, y_axis: 5 },
    { x_axis: 5, y_axis: 7 },
    { x_axis: 5, y_axis: 7 },
    { x_axis: 5, y_axis: 7 },
    { x_axis: 5, y_axis: 7 },
    { x_axis: 6, y_axis: 4 },
  ];

  return (
    <div>
      <LinearHistComponent
        id="component"
        data={data}
        histData={data}
        x_axis="x_axis"
        y_axis="y_axis"
        histValue="x_axis"
        setProps={null}
      ></LinearHistComponent>
    </div>
  );
};

const runHistogramplot = () => {''
  const data = [
    { x_axis: 2, y_axis: 3 },
    { x_axis: 2.32, y_axis: 3.5 },
    { x_axis: 2.34, y_axis: 3.1 },
    { x_axis: 2.555, y_axis: 3.8 },
    { x_axis: 2.56, y_axis: 4 },
    { x_axis: 2.57, y_axis: 4 },
    { x_axis: 3, y_axis: 4 },
    { x_axis: 4, y_axis: 5 },
    { x_axis: 4, y_axis: 5 },
    { x_axis: 4, y_axis: 5 },
    { x_axis: 4, y_axis: 5 },
    { x_axis: 4, y_axis: 5 },
    { x_axis: 4, y_axis: 5 },
    { x_axis: 5, y_axis: 7 },
    { x_axis: 5, y_axis: 7 },
    { x_axis: 5, y_axis: 7 },
    { x_axis: 5, y_axis: 7 },
    { x_axis: 6, y_axis: 4 },
  ];

  return (
    <div>
      <HistogramplotComponent
        id="component"
        data={data}
        value="x_axis"
        xStart={0}
        setProps={null}
      ></HistogramplotComponent>
    </div>
  );
};

const runLinearplot = () => {
  const data = [
    { x_axis: 2, y_axis: 3 },
    { x_axis: 3, y_axis: 4 },
    { x_axis: 4, y_axis: 5 },
    { x_axis: 5, y_axis: 7 },
    { x_axis: 6, y_axis: 4 },
  ];

  return (
    <div>
      <LinearplotComponent
        id="component"
        data={data}
        x_axis="x_axis"
        y_axis="y_axis"
        xStart={0}
        setProps={null}
      ></LinearplotComponent>
    </div>
  );
};

const runScatterplot = () => {
  const [data, setData] = useState(null);

  useEffect(() => {
    d3.tsv(tsvData).then((d) => {
      setData(d);
    });
  }, []);

  function handleButton() {
    const newData = JSON.parse(JSON.stringify(data));
    for (let i = 0; i < 10; i++) {
      newData.pop();
    }
    setData(newData);
  }

  return (
    <div>
      <h1>Web Application</h1>
      {data !== null && (
        <ScatterplotComponent id="component" data={data} setProps={null} />
      )}
      <button onClick={handleButton}>Button</button>
    </div>
  );
};

export default App;
