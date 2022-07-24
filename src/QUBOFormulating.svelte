<script>
  import Link from "../../shared/Link.svelte";
  import Graph from "../../shared/Graph.svelte";
  import Matrix from "../../shared/Matrix.svelte";
  import data1 from "../../stores/Graph_L5_1.js";

  const matrix1 = [
    ["a", "b", "c", "d"],
    ["e", "f", "g", "h"],
    ["i", "j", "k", "l"],
    ["m", "n", "o", "p"],
  ]
</script>

<div class="title">
  <h2>Formulating the QUBO equation</h2>
</div>
<hr />
<div class="text">
  <p>
    From the example tour matrix in the previous lesson, the following rules for occupancy can be derived:
  </p>
  <ol>
    <li>Exactly one occupation per row is allowed (since it is not possible to visit a city more than once)</li>
    <li>Exactly one occupation per column is allowed (since it is not possible to visit multiple cities at the same time)</li>
  </ol>
  <p>
    In this 4x4 grid, the cells are named in alphabetical order. For four cities, the QUBO equation is formulated as follows:
  </p>
  <Matrix data={matrix1} size=200 showLabels={false}/>
  <p>
    {`$$f\\left(a,...,p\\right)=\\left(a+b+c+d-1\\right)^2+\\left(e+f+g+h-1\\right)^2+\\left(i+j+k+l-1\\right)^2+\\left(m+n+o+p-1\\right)^2$$`}
    {`$$+\\left(a+e+i+m-1\\right)^2+\\left(b+f+j+n-1\\right)^2+\\left(c+g+k+o-1\\right)^2+\\left(d+h+l+p-1\\right)^2$$`}
    {`$$=-2a+2ab+2ac+2ad+2ae+2ai+2am-2b+2bc+2bd+2bf+2bj+2bn-2c+2cd+2cg+2ck+2co$$`}
    {`$$-2d+2dh+2dl+2dp-2e+2ef+2eg+2eh+2ei+2em-2f+2fg+2fh+2fj+2fn-2g+2gh+2gk+2go$$`}
    {`$$-2h+2hl+2hp-2i+2ij+2ik+2il+2im-2j+2jk+2jl+2jn-2k+2kl+2ko-2l+2lp-2m+2mn+2mo+2mp$$`}
    {`$$-2n+2no+2np-2o+2op-2p+8$$`}
  </p>
  <p>
    This is a massive and unhandy equation, but a valid cost function since only the correct occupations yield the lowest cost. Since it depends on the number of cities <i>n</i>, the QUBO equation takes <i>n<sup>2</sup></i> variables as its input (meaning it grows at a quadratic rate) and must be reformulated for every individual TSP instance. But this is only half of the story. In order to quantify the second key information of the tours, the route cost must also be considered in the QUBO equation. Luckily, since it is a cost function as well, the values can be adopted and added to the total cost as is. But how to determine which ones to add and when? Consider the following example:
  </p>
  <div align="center"><img width="220" src="/img/MatrixArrows.png" alt="A Tour Matrix where from each node, arrows point to all possible destinations in the next timestamp"></div>
  <p>
    A given edge is taken if its initial vertex is marked in one column and its destination vertex in the following column. Here, the arrows denote all edges that go from <span class="emphasis">B</span> to the other vertices. Since we initially don't know when we're going to visit <span class="emphasis">B</span>, this has to be repeated for all time steps. For example, the edge <span style="text-decoration: overline">BA</span> with the cost of 6.6 is corresponding with <span class="emphasis">(e, b)</span>, <span class="emphasis">(f, c)</span>, <span class="emphasis">(g, d)</span>, and <span class="emphasis">(h, a)</span>. If we multiply this cost with those pairs of variables (this is compliant with the rules of QUBO problems), it is only added if both fields are visited, i.e. equal to <span class="emphasis">1</span>. Additionally, there is no danger of adding the cost of a specific edge more than once because, since it is forbidden to visit a city more than once, only one of these four cases will ever occur, if any. So this is what the second half of the QUBO equation looks like:
    {`$$6.6af+6.6bg+6.6ch+6.6de+5.4aj+5.4bk+5.4cl+5.4di+4.0an+4.0bo+4.0cp+4.0dm+6.6eb+6.6fc$$`}
    {`$$+6.6gd+6.6ha+1.6ej+1.6fk+1.6gl+1.6hi+3.6en+3.6fo+3.6gp+3.6hm+5.4ib+5.4jc+5.4kd+5.4la$$`}
    {`$$+1.6if+1.6jg+1.6kh+1.6le+3.2in+3.2jo+3.2kp+3.2lm+4.0mb+4.0nc+4.0od+4.0pa+3.6mf+3.6ng$$`}
    {`$$+3.6oh+3.6pe+3.2mj+3.2nk+3.2ol+3.2pi$$`}
    This part just gets added to the rest of the equation and must also be re-generated for every TSP instance. Now, this cost function will yield the best (lowest) energy if the formal rules of occupancy, i.e. 1/row and 1/column are satisfied <i>and</i> the quantum annealer chooses those connections whose sum is minimal, according to the TSP requirements (keep this statement in mind; we will discuss in the next section why this isn't that simple).
  </p>
  <div align="center"><strong>We've successfully turned the Traveling Salesman problem into an annealer-compatible QUBO problem!</strong></div>
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
