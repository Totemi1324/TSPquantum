<script>
  import Link from "../../shared/Link.svelte";
</script>

<div class="title">
  <h2>Possible improvements and optimizations</h2>
</div>
<hr />
<div class="text">
  <p>
    The presentation and evaluation of the method is completed; however, it should be considered more as a basis for further algorithmic approaches of this kind and can be further optimized and extended with a few adjustments.
  </p>
  <p>
    Since TSP solutions are closed loops that visit every city, the starting point can be set arbitrarily. So in theory, if we take this decision away from the quantum annealer and set the starting point to, say, <span class="emphasis">A</span>, the first row and column of the Tour matrix can be omitted, since this city is guaranteed not to be visited in the rest of the path:
  </p>
  <div align="center"><img width="250" src="/img/MatrixOptimal.png" alt=""></div>
  <p>
    In addition, the cost function needs to be adjusted so the path from <span class="emphasis">A</span> to <span class="emphasis">B</span>, <span class="emphasis">A</span> to <span class="emphasis">C</span> etc. is only dependent on the second node visited. This approach reduces the size of the Tour Matrix by 1, meaning the number of cities the annealer can find a solution for can be increased by 1 beyond its normal computing capability. However, these and other optimizations are only worthwhile in the long term if they can actually reduce the number of non-zero entries in the Hamiltonian.
  </p>
  <p>
    To make the algorithm more applicable for real-life situations, it would also be possible to extend it beyond the scope of the traditional Traveling Salesman Problem for <i>incomplete graphs</i> (where not all nodes are interconnected) and <i>directed graphs</i> (where certain edges can only be traversed in one direction or have different costs depending on the traversing direction):
  </p>
  <div align="center"><img width="600" src="/img/Graphs.png" alt=""><br><i>Examples of an incomplete graph (left) and a directed graph (right)</i></div>
  <p>
    If a connection between a pair of cities doesn't exists (for example because of a road network layout), the quantum annealer has to be discouraged at all costs from incorporating it in the solution. To represent a non-existent edge, you therefore could assign a massive punishment to it so that the lowest cost is never reached if it's part of the tour. In mathematical literature, this is commonly expressed with an "&#8734;" (infinity) symbol, but in our case, a high integer number is more applicable.
    {`$$H=\\begin{bmatrix}-2 & 2 & 2 & 2 & 2 & \\infty & 0 & \\infty & \\cdots & 4 \\\\ 0 & -2 & 2 & 2 & \\infty & 2 & \\infty & 0 & \\cdots & 0 \\\\ 0 & 0 & -2 & 2 & 0 & \\infty & 2 & \\infty & \\cdots & 4 \\\\ 0 & 0 & 0 & -2 & \\infty & 0 & \\infty & 2 & \\cdots & 2 \\\\ 0 & 0 & 0 & 0 & -2 & 2 & 2 & 2 & \\cdots & 3.6 \\\\ 0 & 0 & 0 & 0 & 0 & -2 & 2 & 2 & \\cdots & 0 \\\\ 0 & 0 & 0 & 0 & 0 & 0 & -2 & 2 & \\cdots & 3.6 \\\\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & -2 & \\cdots & 2 \\\\ \\vdots & \\vdots & \\vdots & \\vdots & \\vdots & \\vdots & \\vdots & \\vdots & \\ddots & \\vdots \\\\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & \\cdots & -2\\end{bmatrix}\\Rightarrow\\begin{bmatrix}-2 & 2 & 2 & 2 & 2 & 100 & 0 & 100 & \\cdots & 4 \\\\ 0 & -2 & 2 & 2 & 100 & 2 & 100 & 0 & \\cdots & 0 \\\\ 0 & 0 & -2 & 2 & 0 & 100 & 2 & 100 & \\cdots & 4 \\\\ 0 & 0 & 0 & -2 & 100 & 0 & 100 & 2 & \\cdots & 2 \\\\ 0 & 0 & 0 & 0 & -2 & 2 & 2 & 2 & \\cdots & 3.6 \\\\ 0 & 0 & 0 & 0 & 0 & -2 & 2 & 2 & \\cdots & 0 \\\\ 0 & 0 & 0 & 0 & 0 & 0 & -2 & 2 & \\cdots & 3.6 \\\\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & -2 & \\cdots & 2 \\\\ \\vdots & \\vdots & \\vdots & \\vdots & \\vdots & \\vdots & \\vdots & \\vdots & \\ddots & \\vdots \\\\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & \\cdots & -2\\end{bmatrix}$$`}
  </p>
  <p>
    To represent different costs at different traversing directions in a directed graph, you only have to differentiate between the order the nodes can be visited when formulating the QUBO equation. In the example below, the cost function has different values depending on whether the path leads from A to C or from C to A:
  </p>
  <div align="center"><img width="200" src="/img/MatrixDirected.png" alt="Excerpt of a Tour Matrix where arrows indicate the connections from node A to C and from node C to A"></div>
  <p>
    {`$$\\Rightarrow f\\left(a,b,...,i,j\\right)=...+3aj+5ib+...$$`}
    The previous method can be applied to the case when a connection exists only in one direction: The other direction is assigned a high cost. It should be noted, however, that in the case of incomplete and directed graphs, the quantum annealer can only output a valid solution if a Hamiltonian cycle actually exists.
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
