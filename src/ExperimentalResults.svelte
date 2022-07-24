<script>
    import BarChart from "../../shared/BarChart.svelte";
    import Link from "../../shared/Link.svelte";

    import bar1 from "../../stores/Bar_L9_1.js";
    import bar2 from "../../stores/Bar_L9_2.js";
    import bar3 from "../../stores/Bar_L9_3.js";
    import bar4 from "../../stores/Bar_L9_4.js";
    import bar5 from "../../stores/Bar_L9_5.js";
    import bar6 from "../../stores/Bar_L9_6.js";
    import bar7 from "../../stores/Bar_L9_7.js";
    import bar8 from "../../stores/Bar_L9_8.js";
    import bar9 from "../../stores/Bar_L9_9.js";
    import bar10 from "../../stores/Bar_L9_10.js";
</script>

<div class="title">
  <h2>Experimental results</h2>
</div>
<hr />
<div class="text">
  <p>
    When it comes to evaluating the performance of quantum algorithms, this often poses a problem because of the inherent non-deterministic nature of this method. Due to the work with quantum states, there is always a portion of randomness involved. In the following sections, we therefore explore how efficient solving the Traveling Salesman Problem on quantum computers really is and how we can improve on this performance.
  </p>
  <p>
    The first problem emerges when trying to quantify TSPs, the underlying mathematical problem. In order to be comparable, a uniform benchmark for graphs of arbitrary size is needed. One way to address this issue is to use graphs in the shape of regular polygons to test the quantum algorithm, starting with a triangle (since it is the simplest shape with a valid Hamiltonian cycle) up to an octagon:
  </p>
  <div align="center"><img width="700" src="/img/Benchmarks.png" alt="Different sized graphs for evaluating the TSP solver, ranging from a triangle to an octagon"></div>
  <p>
    Here, regular polygons with an edge length of 50 units each were used; the coordinates of the corner points can be calculated using e.g. a graphing calculator. These shapes are then converted to the respective Hamiltonian matrices, scaling the costs to 1% (0.5) and the coefficients to 8. For example, the triangle transforms into the following:
    {`$$H=\\begin{bmatrix}-8.0 & 8.0 & 8.0 & 8.0 & 0.5 & 0.5 & 8.0 & 0.5 & 0.5 \\\\ 0.0 & -8.0 & 8.0 & 0.5 & 8.0 & 0.5 & 0.5 & 8.0 & 0.5 \\\\ 0.0 & 0.0 & -8.0 & 0.5 & 0.5 & 8.0 & 0.5 & 0.5 & 8.0 \\\\ 0.0 & 0.0 & 0.0 & -8.0 & 8.0 & 8.0 & 8.0 & 0.5 & 0.5 \\\\ 0.0 & 0.0 & 0.0 & 0.0 & -8.0 & 8.0 & 0.5 & 8.0 & 0.5 \\\\ 0.0 & 0.0 & 0.0 & 0.0 & 0.0 & -8.0 & 0.5 & 0.5 & 8.0 \\\\ 0.0 & 0.0 & 0.0 & 0.0 & 0.0 & 0.0 & -8.0 & 8.0 & 8.0 \\\\ 0.0 & 0.0 & 0.0 & 0.0 & 0.0 & 0.0 & 0.0 & -8.0 & 8.0 \\\\ 0.0 & 0.0 & 0.0 & 0.0 & 0.0 & 0.0 & 0.0 & 0.0 & -8.0\\end{bmatrix}$$`}
  </p>
  <p>
    Using this structure, two problem sets were created: <i>Simple problems</i> where the costs are emitted (so the annealer's only task is to find a valid tour) and <i>complex problems</i> with the costs of the edges included. A major advantage of using polygons is that since the shortest path is always around the edges, the optimal cost can be easily calculated beforehand using this formula, given that <span class="emphasis">C<sub>n</sub></span> is the cost function for a polygon with <i>n</i> corners:
    {`$$\\min C_{n}\\left(q\\right)=-8n+0.5n=-7.5n$$`}
  </p>
  <p>
    Now, the test cases are ready to be fed to the quantum annealer. But before performing the actual benchmark, we have to tune the hyperparameters, i.e. the static parameters that impact the algorithm performance and do not get changed during the calculations. The ones most important to our problem are <span class="emphasis">chain_strength</span> and <span class="emphasis">annealing_time</span>. According to the <Link target="https://docs.ocean.dwavesys.com/projects/system/en/stable/reference/generated/dwave.system.composites.EmbeddingComposite.sample.html#dwave.system.composites.EmbeddingComposite.sample" newPage={true}>Reference Documentation</Link>, <span class="emphasis">chain_strength</span> represents the "coupling strength between qubits that form a chain" on the QPU, meaning the magnitude of the magnetic fields that function as couplers forcing qubits to assume identical values. Similarly, <span class="emphasis">annealing_time</span> sets the time the qubits are allowed to anneal to their optimal energy state before reading them and causing the superposition to collapse. For each of these values, there exist prevailing rules of thumb, but they need not always be the best ones. The optimization process is lengthy and needs a lot of data; if you are interested in the detailed procedure and results, you can get them at the <strong style="color: #2eb6e8;">Downloads</strong> tab of this site.
  </p>
  <p>
    After the hyperparameters have been optimized, it's time to evaluate the overall effectiveness of the quantum solution method. To achieve this, every polygon size of both problem sets was evaluated by the state-of-the-art <i>D-Wave Advantage</i> (Pegasus architecture, 5640 qubits) and the older <i>D-Wave 200Q</i> (Chimera architecture, 2048 qubits) systems with 10 random generated embeddings each. As a comparison to traditional computing, the problems were also submitted to a <i>Simulated Annealing</i> algorithm, which is a widely used heuristic approach to optimization problems that changes the parameters of a problem through random permutations and uses a cooling function to decide whether to keep or discard these<sup>1</sup>. A full explanation would go beyond the scopes of this course, but if you want to learn more about the procedure in detail, you can read about its applications in TSPs <Link target="https://www.fourmilab.ch/documents/travelling/anneal/" newPage={true}>here</Link>.
  </p>
  <p>
    Finally, the following graphs present the results of the different approaches in comparison. Since we're not after relative performance comparisons over a spectrum of values like in the experiments before, we'll only keep the best solution yielded by the reads and calculate difference to the optimal solution instead of the success rate. First, let's look at the energy deltas, that is, the amount of energy by which the quantum annealer missed the optimal solution (therefore, lower values are better). The bars indicate the arithmetic mean of 10 experimental results:
  </p>
  <div class="subtitle">Advantage</div>
  <div class="subplots">
    <BarChart
      points={bar1.points}
      yTicks={bar1.yTicks}
      yLabel="Simple problem"
      width="300"
      height="300"
      barColor="#2eb6e8"
    />
    <BarChart
      points={bar2.points}
      yTicks={bar2.yTicks}
      yLabel="Complex problem"
      width="300"
      height="300"
      barColor="#2eb6e8"
    />
  </div>
  <div class="subtitle">2000Q</div>
  <div class="subplots">
    <BarChart
      points={bar3.points}
      yTicks={bar3.yTicks}
      yLabel="Simple problem"
      width="300"
      height="300"
      barColor="#1a91bc"
    />
    <BarChart
      points={bar4.points}
      yTicks={bar4.yTicks}
      yLabel="Complex problem"
      width="300"
      height="300"
      barColor="#1a91bc"
    />
  </div>
  <div class="subtitle">Simulated Annealing</div>
  <div class="subplots">
    <BarChart
      points={bar1.points}
      yTicks={bar1.yTicks}
      yLabel="Simple problem"
      width="300"
      height="300"
      barColor="#f1b6e8"
    />
    <BarChart
      points={bar1.points}
      yTicks={bar1.yTicks}
      yLabel="Complex problem"
      width="300"
      height="300"
      barColor="#f1b6e8"
    />
  </div>
  <p>
    Next, the times needed for solving:
  </p>
  <div class="subtitle">Advantage</div>
  <div class="subplots">
    <BarChart
      points={bar5.points}
      yTicks={bar5.yTicks}
      yLabel="[ms] Simple problem"
      width="300"
      height="300"
      barColor="#2eb6e8"
    />
    <BarChart
      points={bar6.points}
      yTicks={bar6.yTicks}
      yLabel="[ms] Complex problem"
      width="300"
      height="300"
      barColor="#2eb6e8"
    />
  </div>
  <div class="subtitle">2000Q</div>
  <div class="subplots">
    <BarChart
      points={bar7.points}
      yTicks={bar7.yTicks}
      yLabel="[ms] Simple problem"
      width="300"
      height="300"
      barColor="#1a91bc"
    />
    <BarChart
      points={bar8.points}
      yTicks={bar8.yTicks}
      yLabel="[ms] Complex problem"
      width="300"
      height="300"
      barColor="#1a91bc"
    />
  </div>
  <div class="subtitle">Simulated Annealing</div>
  <div class="subplots">
    <BarChart
      points={bar9.points}
      yTicks={bar9.yTicks}
      yLabel="[ms] Simple problem"
      width="300"
      height="300"
      barColor="#f1b6e8"
    />
    <BarChart
      points={bar10.points}
      yTicks={bar10.yTicks}
      yLabel="[ms] Complex problem"
      width="300"
      height="300"
      barColor="#f1b6e8"
    />
  </div>
  <p>
    This experiments immediately show the downside of Simulated Annealing, similar to other traditional computing methods: Whereas it is able to find optimal solutions for large problem sizes, the time needed for computation is very lengthy, more than 10 minutes in most cases. The quantum annealers on the other hand are able to solve the same tasks in just fragments of a second. The newer D-Wave Advantage model is faster than the 2000Q across all problem sizes, but the computing time varies more greatly and is less consistent. In summary, our quantum algorithm can find at least one correct solution for every problem size and complexity except for the n=8 complex problem.
  </p>
  <p>
    All Python files used to perform the experiments as well as the raw measurement data can be accessed at <Link target="https://github.com/Totemi1324/TSPquantum" newPage={true}>the project's GitHub repo</Link> and at the <strong style="color: #2eb6e8;">Downloads</strong> section.
  </p>
</div>
<hr>
<div class="refs">
  <h3>References</h3>
  <ol>
    <li><Link target="https://en.wikipedia.org/wiki/Simulated_annealing" newPage={true}>https://en.wikipedia.org/wiki/Simulated_annealing</Link>, accessed: 12.05.2022</li>
  </ol>
</div>

<style>
  .title h2, .refs h3 {
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
  .subtitle {
    color: #bbb;
    text-align: center;
    font-style: italic;
  }
  .subplots {
    display: flex;
  }
</style>