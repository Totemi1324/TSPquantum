<script>
    import Matrix from "../../shared/Matrix.svelte";
    import Graph from "../../shared/Graph.svelte";
    import data1 from "../../stores/Graph_L5_2.js";

    const matrix1 = [
        [0, 0, 0, 1],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [1, 0, 0, 0]
    ]
</script>

<div class="title">
  <h2>From coefficients to the Hamiltonian</h2>
</div>
<hr />
<div class="text">
  <p>
    It's time to assemble: As discussed in Chapter 2, the coefficients from the QUBO equation need to be transferred to the Hamiltonian in order to be a valid input for the quantum annealer. The result of our calculations is a pretty massive matrix of the size 16x16 from which an excerpt is shown below:
    {`$$H=\\begin{bmatrix}h_a & h_{ab} & h_{ac} & h_{ad} & h_{ae} & h_{af} & h_{ag} & h_{ah} & \\cdots & h_{ap} \\\\ 0 & h_{b} & h_{bc} & h_{bd} & h_{be} & h_{bf} & h_{bg} & h_{bh} & \\cdots & h_{bp} \\\\ 0 & 0 & h_{c} & h_{cd} & h_{ce} & h_{cf} & h_{cg} & h_{ch} & \\cdots & h_{cp} \\\\ 0 & 0 & 0 & h_{d} & h_{de} & h_{df} & h_{dg} & h_{dh} & \\cdots & h_{dp} \\\\ 0 & 0 & 0 & 0 & h_{e} & h_{ef} & h_{eg} & h_{eh} & \\cdots & h_{ep} \\\\ 0 & 0 & 0 & 0 & 0 & h_{f} & h_{fg} & h_{fh} & \\cdots & h_{fp} \\\\ 0 & 0 & 0 & 0 & 0 & 0 & h_{g} & h_{gh} & \\cdots & h_{gp} \\\\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & h_{h} & \\cdots & h_{hp} \\\\ \\vdots & \\vdots & \\vdots & \\vdots & \\vdots & \\vdots & \\vdots & \\vdots & \\ddots & \\vdots \\\\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & \\cdots & h_{p}\\end{bmatrix}=\\begin{bmatrix}-2 & 2 & 2 & 2 & 2 & 6.6 & 0 & 6.6 & \\cdots & 4 \\\\ 0 & -2 & 2 & 2 & 6.6 & 2 & 6.6 & 0 & \\cdots & 0 \\\\ 0 & 0 & -2 & 2 & 0 & 6.6 & 2 & 6.6 & \\cdots & 4 \\\\ 0 & 0 & 0 & -2 & 6.6 & 0 & 6.6 & 2 & \\cdots & 2 \\\\ 0 & 0 & 0 & 0 & -2 & 2 & 2 & 2 & \\cdots & 3.6 \\\\ 0 & 0 & 0 & 0 & 0 & -2 & 2 & 2 & \\cdots & 0 \\\\ 0 & 0 & 0 & 0 & 0 & 0 & -2 & 2 & \\cdots & 3.6 \\\\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & -2 & \\cdots & 2 \\\\ \\vdots & \\vdots & \\vdots & \\vdots & \\vdots & \\vdots & \\vdots & \\vdots & \\ddots & \\vdots \\\\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & \\cdots & -2\\end{bmatrix}$$`}
    So the problem is solved, right? Unfortunately, not quite. There is one issue left we have to talk about: the scaling. If we try to send this Hamiltonian to the quantum annealer, the results are the following:
  </p>
  <div align="center"><img style="width: 40%" src="/img/Results.png" alt="A list of responses from the quantum annealer where each solution traverses only three cities instead of four"></div>
  <p>
    The table shows the top 5 from the results of the D-Wave annealer (which are sorted from best to worst). A good portion, if not all of them visit only three or even less cities. This is because the coefficients that enforce the annealer to follow the rule "Exactly one occupation per row/column" are -2 or 2 and therefore too small compared to the distances between the vertices that range from 3 to 7. If the annealer occupies less cells, the energy it saves by omitting edges far outweighs the punishment it receives for visiting less cities. To fix this problem, we have to scale our coefficients accordingly: If we multiply all coefficients by the same factor, the relations are preserved, which means that we can scale certain parts of the equation to emphasize them more. As a general rule of thumb, if <span class="emphasis">s</span> = the length of the longest possible tour in the graph and <span class="emphasis">n</span> = the number of cities, all coefficients that enforce the first rule should be calculated as follows:
    {`$$c = \\pm \\frac{3s}{n}$$`}
    Now, our Hamiltonian solves the TSP correctly for all sizes! Here is a visualization of the Hamilton matrix for a big TSP with <span class="emphasis">n = 8</span>:
  </p>
  <div align="center"><img style="width: 25%" src="/img/Visualization.png" alt="A visualization of a 64x64 Hamiltonian where the values are represented with different colors"></div>
  <h3>How to evaluate the results</h3>
  <p>
    The updated Hamiltonian of the <span class="emphasis">n = 4</span> example from Lesson 5 now yields the following solution:
    {`$$q_A=\\left[0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0\\right]\\Rightarrow$$`}
  </p>
  <Matrix data={matrix1} size=200 showLabels={true} />
  <p>
    Now we have to reverse-engineer the tour on the graph: The answer vector <span class="emphasis"><i>q<sub>A</sub></i></span> (which contains the values of the variables <span class="emphasis">a</span> through <span class="emphasis">n</span>) first has to be translated to the tour matrix by transferring the values one-by-one to a 4x4 grid. By attaching the timestep and city labels of the tour matrix, the order of the visited cities becomes visible: <strong> D -> B -> C -> A (-> D)</strong>. Let's look at the graph again: Indeed, it found the shortest path!
  </p>
  <Graph graph={data1} width="500" height="350" style="display: block; margin: 0 auto;"/>
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
