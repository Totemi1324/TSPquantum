<script>
  import Graph from "../../shared/Graph.svelte";
  import Matrix from "../../shared/Matrix.svelte";
  import data1 from "../../stores/Graph_L5_1.js";

  const matrix1 = [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0],
  ]
</script>

<div class="title">
  <h2>Transforming the Traveling Salesman Problem for quantum annealers</h2>
</div>
<hr />
<div class="text">
  <p>
    Now, we have arrived at the main part of the course. Creating a quantum solution for the TSP is an exciting example of the versatility of quantum computing as well as a demonstration of how it can help improve everyday tasks. The first step towards such a method is the question of how to transform the core component of the TSP, the graph, into a QUBO problem.
  </p>
  <p>
    As shown in the previous sections, the easiest way of creating QUBO problems is through a square field with numbered cells. Let's consider the simplest instance of the TSP, a graph of four cities (since this is the minimum number of vertices that allows different solutions than the optimum):
  </p>
  <Graph graph={data1} width="500" height="350" style="display: block; margin: 0 auto;"/>
  <p>
    If we consider <span class="emphasis">A</span> as a starting point, here our tour is <strong>A -> B -> D -> C -> A</strong> (of course, the inverse A -> C -> D -> B -> A is valid, too). How can we transform this data structure to a number field?
  </p>
  <h3>The Tour Matrix</h3>
  <p>
    A possible tour is characterized by two parts of information:
  </p>
  <ol>
    <li>The chronological order of the visited cities</li>
    <li>The total cost of the route, i.e. the sum of the length of the edges taken</li>
  </ol>
  <p>
    By using a matrix, the mathematical concept previously discussed, it is possible to address the first point. Applied to the graph above, the result is this:
  </p>
  <Matrix size="300" data={matrix1} showLabels={true}/>
  <p>
    The rows represent the individual cities, while the columns mark the "points in time", i.e. each step made. An entry of <span class="emphasis">1</span> in the field <span class="emphasis">a<sub>ij</sub></span> means that the <span class="emphasis">i</span>-th city is visited in the <span class="emphasis">j</span>-th time step. The fifth time step would mark the return to the starting city, but since it would always be an exact copy of the first column, it can be omitted to minimize the data. Now, we have created an abstraction that can be applied to tours in graphs of any size. Let's name this new structure <i>tour matrix</i>.
  </p>
  <p>
    Perhaps, you can already see where this is going: Indeed, this looks very similar to the "checkers" example from Section 2. You can think of the <span class="emphasis">1</span>s as the pieces that can be placed on a board to mark which city belongs to which time step. So next, we're going to explore how to extract the QUBO equation.
  </p>
</div>

<style>
  .title h2 {
    background: -webkit-linear-gradient(90deg, #1a91bc, #2eb6e8);
    background-clip: text;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    -webkit-touch-callout: none;
    -webkit-user-select: none;
    -khtml-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
  }
  hr {
    border: 1px solid white;
    border-top: 1px solid #ddd;
    margin: 20px auto;
  }
</style>
