// global d3 //


// instantiate the scrollama
const scroller = scrollama();

// Create Callback functions to access JS Functions or D3 functions

// setup the instance, pass callback functions
scroller
  .setup({
    step: ".step",
  })
  .onStepEnter((response) => {
    // { element, index, direction }
  })
  .onStepExit((response) => {
    // { element, index, direction }
  });

// setup resize event
window.addEventListener("resize", scroller.resize);