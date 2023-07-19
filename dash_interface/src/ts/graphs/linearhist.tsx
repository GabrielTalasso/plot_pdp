import * as d3 from "d3";

export function linearhist(
  pdpData,
  histData,
  element,
  x_axis,
  y_axis,
  histValue,
  setValue?
) {
  d3.select(element).selectAll("*").remove();

  const margin = { top: 20, right: 20, bottom: 30, left: 40 };
  const width = 720 - margin.left - margin.right;
  const height = 375 - margin.top - margin.bottom;
  const heightHist = 120 - margin.top - margin.bottom;

  const xMin = Math.min(
    d3.min(pdpData, (d) => d[x_axis]),
    d3.min(histData, (d) => d[histValue])
  );
  const xMax = Math.max(
    d3.max(pdpData, (d) => d[x_axis]),
    d3.max(histData, (d) => d[histValue])
  );

  const x = d3.scaleLinear().range([0, width]);

  const y = d3.scaleLinear().range([height, 0]);
  const yHist = d3.scaleLinear().range([heightHist, 0]);

  const xAxis = d3.axisBottom(x);

  const yAxis = d3.axisLeft(y);

  function mouseover(event, d) {
    focus.style("opacity", 1);
    focusText.style("opacity", 1);
    focus.attr("x", event.x - 30).attr("y", event.y - 40);
    focusText
      .html(
        "x:" +
          Math.round(d[x_axis] * 10) / 10 +
          "  -  " +
          "y:" +
          Math.round(d[y_axis] * 10) / 10
      )
      .attr("x", event.x - 15)
      .attr("y", event.y - 20);
  }

  function mouseout() {
    focus.style("opacity", 0);
    focusText.style("opacity", 0);
  }

  function mouseClick(event, d) {
    const text =
      "x:" +
      Math.round(d[x_axis] * 10) / 10 +
      "  -  " +
      "y:" +
      Math.round(d[y_axis] * 10) / 10;
    setValue(text);
  }

  const bins = d3
    .bin()
    .thresholds(20)
    .value((d) => Math.round(d[histValue] * 10) / 10)(histData);

  const svg = d3
    .select(element)
    .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

  x.domain([xMin, xMax]);
  y.domain(d3.extent(pdpData, (d) => d[y_axis]));
  yHist.domain([0, d3.max(bins, (d) => d.length)]);

  const focus = svg
    .append("g")
    .append("rect")
    .style("fill", "none")
    .attr("width", 160)
    .attr("height", 40)
    .attr("stroke", "#69b3a2")
    .attr("stroke-width", 4)
    .style("opacity", 0);

  var focusText = svg
    .append("g")
    .append("text")
    .style("opacity", 0)
    .attr("text-anchor", "left")
    .attr("alignment-baseline", "middle")
    .html("lkjdslkfjsd");

  svg
    .append("g")
    .attr("transform", "translate(0," + height + ")")
    .call(xAxis)
    .append("text")
    .attr("x", width)
    .attr("y", -6)
    .style("text-anchor", "end");

  svg
    .append("g")
    .call(yAxis)
    .append("text")
    .attr("transform", "rotate(-90)")
    .attr("y", 6)
    .attr("dy", ".71em")
    .style("text-anchor", "end");

  // svg
  //   .append("g")
  //   .attr("fill", "paleturquoise")
  //   .selectAll()
  //   .data(bins)
  //   .join("rect")
  //   .attr("x", (d) => x(d.x0) + 1)
  //   .attr("width", (d) => x(d.x1) - x(d.x0) - 1)
  //   .attr("y", (d) => yHist(d.length) + height - heightHist)
  //   .attr("height", (d) => yHist(0) - yHist(d.length));

  svg
    .append("path")
    .datum(bins)
    .attr("fill", "paleturquoise")
    .attr("stroke", "steelblue")
    .attr("stroke-width", 1)
    .attr(
      "d",
      d3
        .line()
        .x((d) => x((d.x1 + d.x0) / 2))
        .y((d) => yHist(d.length) + height - heightHist)
        .curve(d3.curveCatmullRom)
    );

  svg
    .append("path")
    .datum(pdpData)
    .attr("fill", "none")
    .attr("stroke", "steelblue")
    .attr("stroke-width", 1.5)
    .attr(
      "d",
      d3
        .line()
        .x((d) => x(d[x_axis]))
        .y((d) => y(d[y_axis]))
    );

  svg
    .selectAll("myCircles")
    .data(pdpData)
    .enter()
    .append("circle")
    .attr("fill", "red")
    .attr("stroke", "none")
    .attr("cx", (d) => x(d[x_axis]))
    .attr("cy", (d) => y(d[y_axis]))
    .attr("r", 3)
    .on("mouseover", mouseover)
    .on("mouseout", mouseout)
    .on("click", mouseClick);
}
