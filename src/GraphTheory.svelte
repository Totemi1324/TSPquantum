<script>
  import Graph from "../../shared/Graph.svelte";
  import data1 from "../../stores/Graph_L2.js";
</script>

<div class="title">
  <h2>Graph theory</h2>
</div>
<hr />
<div class="text">
  <p>
    Computers only take numbers, so we need to use them as well. We already subconsciously drew a key concept of the solving method with the cities interconnected with lines: <i>Graphs</i> are a fundamental part of mathematics, so much so that they have their own field of study called <i>graph theory</i>. In general, a graph describes a set of cities, called <i>"vertices"</i>, and how they are connected mathematically.
  </p>
  <p>
    Let's simplify our example from the lecture before to just 4 cities and name them A, B, C, and D.
  </p>
  <Graph graph={data1} width="500" height="350" style="display: block; margin: 0 auto;"/>
  <p style="text-align: center">
    <i>Fully connected graph with 4 vertices</i>
  </p>
  <p>
    Every node is represented as a blue circle connected to the other nodes through <i>"edges"</i>, the distances between the nodes drawn in gray. In our example, every possible pair of vertices is connected, each edge can be traversed in both directions and each edge has a unique distance value assigned to it. This is called a <strong>complete undirected weighted graph</strong>. Graphs can have various shapes and types, but in this tutorial, we only focus on this one since it corresponds to the standard definition of the TSP.
  </p>
  <p>
    In mathematical terms, a graph like this can be characterized as follows:
    {`$$G=\\left(V,E,d\\right)$$`}
  </p>
  <p style="text-align: center">where</p>
  <p>
    {`$$V=\\left\\{v_1,v_2,...\\right\\}$$`}
    {`$$E\\subseteq\\left\\{\\left\\{v_i,v_j\\right\\}|\\left(v_i,v_j\\right)\\in V^2\\wedge v_i\\neq v_j\\right\\}$$`}
    {`$$d:E\\to\\mathbb{R}$$`}
  </p>
  <p>
    That was quite a lot at once. Let's go through it step-by-step:
  </p>
  <ul>
    <li>A graph <span class="emphasis">G</span> is a combination of three components: <span class="emphasis">V</span>, the vertices, <span class="emphasis">E</span>, the edges, and <span class="emphasis">d</span>, a distance function. The notation in <span class="emphasis">()</span> as a triplet shows that they belong together.</li>
    <li><span class="emphasis">V</span> denotes a set of vertices that are part of the graph. Sets are marked by curly braces <span class="emphasis">&#123;&#125;</span>.</li>
    <li><span class="emphasis">E</span> is a set of edges, which are unordered pairs of vertices &#123;v<sub>i</sub>, v<sub>j</sub>&#125;. The pipe symbol <span class="emphasis">|</span> defines what conditions these pairs must fulfill: Both v<sub>i</sub> and v<sub>j</sub> must be part of V<sup>2</sup> ("squared" for sets means the cartesian product, i.e. the set of all possible combinations of a set's elements) <strong>and</strong> v<sub>i</sub> must not be equal to v<sub>j</sub> to prevent loops.</li>
    <li><span class="emphasis">d</span> is a function that maps every edge (i.e. unordered pair of vertices) to a real number, in this case, the distance.</li>
  </ul>
  <p>
    So, the graph above can be described like this:
    {`$$V=\\left\\{A,B,C,D\\right\\}$$`}
    {`$$E=\\left\\{\\left\\{A,B\\right\\},\\left\\{A,C\\right\\},\\left\\{A,D\\right\\},\\left\\{B,C\\right\\},\\left\\{B,D\\right\\},\\left\\{C,D\\right\\}\\right\\}$$`}
    {`$$d:E\\to\\begin{cases}2.5 & \\text{if }E=\\left\\{A,B\\right\\} \\\\ 3.3 & \\text{if }E=\\left\\{A,C\\right\\} \\\\ 5.7 & \\text{if }E=\\left\\{A,D\\right\\} \\\\ 4.1 & \\text{if }E=\\left\\{B,C\\right\\} \\\\ 3.4 & \\text{if }E=\\left\\{B,D\\right\\} \\\\ 5.6 & \\text{if }E=\\left\\{C,D\\right\\}\\end{cases}$$`}
  </p>
  <p>
    The job of every TSP algorithm is to find a path that visits each vertex exactly once and returns to the starting vertex (also called a <i>closed Hamiltonian cycle</i>) where the sum of the distances from the distance function is as low as possible. Since the goal is to traverse the graph, the TSP is a "graph traversal" problem. 
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
