<script>
  import Link from "../../shared/Link.svelte";
</script>

<div class="title">
  <h2>Where are the constraints?</h2>
</div>
<hr />
<div class="text">
  <p>
    Although the unbeatable speed of this quantum approach makes it very attractive, it also has some major limitations. Some of them are posed by the simple state of today's technology and are likely to be overcome by future advancements in the field of quantum computing. Since a graph of <i>n</i> nodes is first converted to a Tour Matrix of <i>n<sup>2</sup></i> elements and then to a Hamiltonian of <i>(n<sup>2</sup>)<sup>2</sup></i> elements, the number of qubits and connections needed rises quartically, i.e. by an exponent of four. Analogous to traditional computing, you could characterize the <i>complexity</i> of the quantum algorithm as:
    {`$$O\\left(n\\right)\\approx n^4$$`}
  </p>
  <div style="float: right; margin: 0 20px"><img width="300" src="/img/Inspector.png" alt="A visualization of the network of qubits on the QPU that are involved in the calculation of a TSP of size 8"></div>
  <p>
    As the number of interconnected qubits rises, the number of physical qubits that need to be combined to logical qubits increases, causing the probability of false results to grow exponentially. This is why <span class="emphasis">n = 8</span> is approximately the limit of what the current D-Wave Advantage system can solve, as each qubit is connected to 15 others only. With each city added, the embedding also becomes larger, until eventually all the space on the QPU is used up. The figure on the right shows the space the embedding of the problem size <span class="emphasis">n = 8</span> takes up on the QPU, working with chains that span 8-9 qubits in length. However, due to increasing computing capacity and more complex architectures, this limitation will likely become increasingly irrelevant in the future.
  </p>
  <p>
    The <i>matrix density</i>, meaning the proportion of matrix elements that are not zeros, also plays a role in computing efficiency. The sparser the Hamiltonian, i.e. the fewer chains are needed relative to the problem size, the easier it is for the quantum computer to solve the QUBO problem. Since the matrices produced by this quantum TSP algorithm are relatively dense, the performance limit is reached with smaller problem sizes than usual. This problem is far more relevant since it is not yet foreseeable whether the accuracy problems of quantum annealers will be solved by scaling alone.
  </p>
  <h3>A solution approach: Controlling the embedding</h3>
  <p>
    When submitting problems to the QPU, the embedding is generated automatically by D-Wave Ocean to save time, especially in the case of larger problems. However, this is a complex optimization task as well which is why algorithms are likely to not find the best solution. If we wanted to maximize the efficiency, it therefore would be theoretically possible to manually embed the QUBO problem and to set each qubit and connection by hand. If you are interested in the technical side, you can read about it in detail in the <Link target="https://docs.ocean.dwavesys.com/en/stable/concepts/embedding.html" newPage={true}>official documentation</Link>.
  </p>
  <p>
    This task however requires not only a large amount of further mathematical calculations, but also an intricate and founded knowledge of the QPU topology. The process is time-consuming and has to be repeated for each individual problem size, making it only worthwhile for some small problems.
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
