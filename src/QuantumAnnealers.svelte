<script>
  import Link from "../../shared/Link.svelte";
  import Matrix from "../../shared/Matrix.svelte"

  const matrix1 = [
    [1, 4, 2, 1],
    [3, 0, 3, 1],
    [5, 1, 2, 0],
    [4, 1, 2, 3],
  ]
  const matrix2 = [
    [-3, 2, 2, 2],
    [0, -3, 2, 2],
    [0, 0, -3, 2],
    [0, 0, 0, -3],
  ]
</script>

<div class="title">
  <h2>How do quantum annealers work?</h2>
</div>
<hr />
<div class="text">
  <p>
    Equipped with the basic mathematics, we can now face the question: How do we get from an input to a result? The process of programming a quantum annealer differs greatly from that of a traditional computer since it takes numbers rather than instructions or lines of code. Here is a depiction of this procedure:
  </p>
  <div align="center"><img width="700" src="/img/Process.png" alt="A Hamilton matrix titled Input points to the D-Wave Advantage quantum annealer points to a vector titled Output"></div>
  <p>
    This may look a bit confusing, so let's tackle it step-by-step.
  </p>
  <h3>Vectors and matrices</h3>
  <p>
    To represent our data, we need yet another mathematical construct. In its traditional form, a vector is a quantity in space with a direction and length (often represented as an arrow or ray)<sup>1</sup> and consists of two or more coordinates written in a vertical column. For example, a vector in 3-dimensional space would contain three coordinates:
    {`$$\\vec{ q }=\\begin{pmatrix}q_1 \\\\ q_2 \\\\ q_3\\end{pmatrix}$$`}
    As a vector holds an array of numbers, we can utilize vectors to retrieve our results from the quantum annealer. If we had a 4x4 board with 4<sup>2</sup>=16 fields, the entries would denote whether our fields <span class="emphasis">a</span>, <span class="emphasis">b</span>, etc. through <span class="emphasis">n</span> should be occupied (1) or not (0). This is defined as the <strong>answer vector q<sub>A</sub></strong>.
    {`$$\\vec{q}_A = \\begin{pmatrix}a \\\\ b \\\\ \\vdots \\\\ n\\end{pmatrix} = \\begin{pmatrix}0 \\\\ 1 \\\\ \\vdots \\\\ 1\\end{pmatrix}$$`}
    Similarly, think of a <i>matrix</i> as a series of vectors glued together. It is a rectangular field of numbers where each element is indexed in the format <span class="emphasis">a<sub>ij</sub></span> (<span class="emphasis">i</span> and <span class="emphasis">j</span> denote the row and column index of a given element).
  </p>
  <Matrix size="200" data={matrix1} showLabels={false}/>
  <p>
    For example, the element a<sub>31</sub> of the matrix above is 5.
  </p>
  <p>
    Don't worry if it is not fully clear yet, we will use matrices only as a simple means to an end. Remember the QUBO equations from the previous lesson? In fact, matrices are the only way to pass those as an input to the quantum annealer. Since the form of QUBO equations is always the same, we can concatenate the coefficients (the only values that change) in a matrix of the following format to create a representation of our problem's definition:
    {`$$f\\left(a,b,c,d\\right)=h_aa+h_bb+h_cc+h_dd+h_{ab}ab+h_{ac}ac+h_{ad}ad+h_{bc}bc+h_{bd}bd+h_{cd}cd$$`}
    {`$$\\Rightarrow H=\\begin{pmatrix}h_a & h_{ab} & h_{ac} & h_{ad} \\\\ 0 & h_b & h_{bc} & h_{bd} \\\\ 0 & 0 & h_c & h_{cd} \\\\ 0 & 0 & 0 & h_d\\end{pmatrix}$$`}
    This is the definition of the <strong>Hamilton matrix H</strong>, or just <strong>Hamiltonian</strong>. In its main diagonal (the fields where <span class="emphasis">i</span> and <span class="emphasis">j</span> are equal) are the coefficients of the individual fields and next to them those of the connections to other fields. Because the lower half remains empty and is filled with zeros, the Hamiltonian belongs to the type of <i>upper triangular matrices</i>. If we take our "boardgame" example from the previous lesson with the QUBO problem "Exactly two out of four fields should be occupied", this is the resulting Hamiltonian:
    {`$$f\\left(a,b,c,d\\right)=-3a-3b-3c-3d+2ab+2ac+2ad+2bc+2bd+2cd\\Rightarrow$$`}
  </p>
  <Matrix size="150" data={matrix2} showLabels={false}/>
  <p>
    Now, we said that a quantum annealer tries to find the answer vector whose coordinates give the lowest cost. Since we compressed the cost function, which was our QUBO problem, into a matrix, the operation can be reformulated as follows<sup>2</sup>:
    {`$$\\min C\\left(q\\right)=\\min_{q_i=0,1}\\left(\\sum_{i=1}^{N}a_iq_i+\\sum_{i<j}^{N}b_{ij}q_iq_j\\right)=\\min\\left(\\vec{q}^TH\\vec{q}\\right)$$`}
    This looks more complicated than it is and just tells us that we want to minimize the cost <span class="emphasis">C</span> which consists of two sums, namely the products of each coefficient <span class="emphasis">a<sub>i</sub></span> with its respective field <span class="emphasis">q<sub>i</sub></span> and the other coefficients <span class="emphasis">b<sub>ij</sub></span> with any pair of two fields <span class="emphasis">q<sub>i</sub></span> and <span class="emphasis">q<sub>j</sub></span>. Alternatively, we can consider the operation as a matrix multiplication, where the Hamiltonian is multiplied from the right with the answer vector and from the left with the transformed (i.e. horizontal) answer vector.
  </p>
  <div align="center"><strong>Congratulations! You now understand how a quantum annealer solves problems.</strong></div>
  <h3>The inner workings</h3>
  <p>
    But how does a quantum annealer work on the inside? This is a more complicated subject, which we can only treat superficially here without having advanced knowledge of quantum physics.
  </p>
  <div style="float: right"><img width="150" src="/img/Qpu.png" alt="A quantum processing unit on a chipset"></div>
  <p>
    The heart of a quantum annealer is the <i>QPU</i> (Quantum Processing Unit<sup>3</sup>), a few square centimeters large chip, which is equipped with the quantum mechanical counterparts of the bits, <i>qubits</i>. In contrast to classical computers, these are not realized with transistors but with artificial atoms of a certain spin, which allows them to assume two states simultaneously (<i>spin up</i> and <i>spin down</i>) according to the rules of quantum physics until they are measured. The quantum annealer derives its potentially enormous computing power from this state called <i>superposition</i>.
  </p>
  <p>
    The current model <i>D-Wave Advantage</i> has exactly 5627 qubits. These are interconnected with so-called <i>couplers</i>, which allow the qubits to interact with each other. The number of couplers per qubit ultimately determines the computing power of the annealer.
  </p>
  <div align="center"><img width="600" src="/img/ChimeraPegasus.png" alt="Dots connected by lines to represent the QPU topology of the D-Wave quantum annealers"><br><i>The graphs of the (a) Chimera architecture of the D-Wave 2000Q and the newer (b) Pegasus architecture show the differences between the QPU's structures. (a) has 6 couplers/qubit, (b) 15 couplers/qubit<sup>4</sup></i></div>
  <p>
    These couplers consist of magnetic fields that can be tweaked individually, so that after a measurement, a qubit is more likely to become <span class="emphasis">1</span> or <span class="emphasis">0</span>, respectively, and pairs of qubits are more likely to assume equal or unequal values. When the quantum annealer receives a Hamiltonian, it sets the coefficients <span class="emphasis">a<sub>i</sub></span> and <span class="emphasis">b<sub>ij</sub></span> as the strength of these magnetic fields also called <i>bias</i>. For the annealer to work, the QPU must be cooled to a temperature near absolute zero (16mK, approx. -273.1°C). Through an effect known as <i>quantum tunneling</i>, the qubits in this system try to anneal the state of the lowest energy, which, through the programming of the couplers, is the best solution for the original optimization problem. That is the reason why a cost function is needed: It determines the state of "lowest cost" (or "lowest energy").
  </p>
</div>
<hr>
<div class="refs">
  <h3>References</h3>
  <ol>
    <li><Link target="https://en.wikipedia.org/wiki/Vector_(mathematics_and_physics)" newPage={true}>https://en.wikipedia.org/wiki/Vector_(mathematics_and_physics)</Link>, accessed: 18.03.2022</li>
    <li>M. Willsch, D. Willsch, K. Michielsen. <i>Lecture notes: Programming Quantum Computers</i>. arXiv: 2201.02051 (2022), accessed: 19.03.2022</li>
    <li>Fiona H, <i>New QPU Solver: Advantage Performance Update</i>, (2021), <Link target="https://support.dwavesys.com/hc/en-us/articles/4410049473047-New-QPU-Solver-Advantage-Performance-Update" newPage={true}>https://support.dwavesys.com/hc/en-us/articles/4410049473047-New-QPU-Solver-Advantage-Performance-Update</Link>, accessed: 20.03.2022</li>
    <li>Fig. 2, C. Gonzales Calaza, D. Willsch, K. Michielsen. <i>Garden optimization problems for benchmarking quantum annealers</i>. arXiv: 2101.10827 (2021), accessed: 20.03.2022</li>
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
</style>
