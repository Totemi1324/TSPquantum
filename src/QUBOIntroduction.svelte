<script>
  import Matrix from "../../shared/Matrix.svelte";

  const matrix1 = [
    ["a", "b"],
    ["c", "d"],
  ];
</script>

<div class="title">
  <h2>QUBO-problems</h2>
</div>
<hr>
<div class="text">
  <p>
    Before we can explore how quantum annealers work, there is an essential basic to be covered. For a quantum annealer to solve a task, it must be defined as a <strong>quadratic unconstrained binary optimization problem</strong> or <strong>QUBO problem</strong> for short. This isn't particularly helpful, so let's break it down:
  </p>
  <ul>
    <li><i>Quadratic</i> means a maximum of two variables can be multiplied.</li>
    <li><i>Unconstrained</i> means the correct answer is not constrained by other conditions.</li>
    <li><i>Binary</i> means we can insert 0 or 1 only.</li>
    <li><i>Optimization</i> is – if you remember from the previous lessons – the process of finding the optimal solution to a complex problem with approximation.</li>
  </ul>
  <p>
    The QUBO form is another mathematical construct that aids the quantum annealer in utilizing the physical properties of its qubits. Let's look at an example to illustrate the concept.
  </p>
  <i style="color: #aaa">
    Sidenote: The following is only one possible type of QUBO problem, but since it is closest to the TSP, it is the only one covered in this course. Also, there are other ways of programming a quantum annealer, like Ising problems, which we will omit for the sake of conciseness.
  </i>
  <div align="center"><img width="150" src="/img/Checkers.png" alt="A checkers board with fields labeled a, b, c and d, above it four pieces"></div>
  <Matrix size="150" data={matrix1} showLabels={false} />
  <p>
    This 2x2 checkers board has the four fields <span class="emphasis">a</span>, <span class="emphasis">b</span>, <span class="emphasis">c</span>, and <span class="emphasis">d</span>. Additionally, there are four pieces, each of which can, but doesn't have to be placed on any field (but not multiple on the same field). When a field is occupied, it is represented as <strong>1</strong>, otherwise as a <strong>0</strong>. The quantum computer should place the pieces so that as many fields as possible are occupied.
  </p>
  <p>
    Again: A computer needs numbers. Is there a way to tell how good a particular solution is? All optimization problems require a <strong>cost function</strong>, which rates a solution's correctness: The lower the cost, the better. Now, our goal shifted from finding the best solution to minimizing the cost function. If we have a QUBO problem that takes four variables <span class="emphasis">a</span>, <span class="emphasis">b</span>, <span class="emphasis">c</span>, and <span class="emphasis">d</span> (which are either 0 or 1) as an input, the cost function is defined as follows:
    {`$$f\\left(a,b,c,d\\right)=h_aa+h_bb+h_cc+h_dd+h_{ab}ab+h_{ac}ac+h_{ad}ad+h_{bc}bc+h_{bd}bd+h_{cd}cd$$`}
    First, we sum up the values of all fields, then we add the product of each possible <i>pair</i> of the field values. The <span class="emphasis">h</span> with which the field values are multiplied are simple coefficients, i.e. real numbers, that control how much we want to reward (or punish) the individual occupancies. This is quite a clever system: If a field is unoccupied, meaning 0, it eliminates the corresponding coefficient from the equation. Similarly, in the pairs of fields, a reward only stays in the equation if both fields are 1. Since we are searching for the lowest cost, <span class="emphasis">h &#60; 0</span> means "reward", <span class="emphasis">h &#62; 0</span> "punishment" and <span class="emphasis">h = 0</span> "irrelevant". For example: If we really want <span class="emphasis">a</span> to be occupied, we can give it an <span class="emphasis">h</span> of -10, or if we want to prevent that <span class="emphasis">b</span> and <span class="emphasis">c</span> are occupied simultaneously, <span class="emphasis">h</span> should be a high positive number like 25.
  </p>
  <p>
    Now we can define a QUBO problem for our original task: As many fields as possible should be occupied.
    {`$$f\\left(a,b,c,d\\right)=(-1)\\times a+(-1)\\times b+(-1)\\times c+(-1)\\times d=-a-b-c-d$$`}
    We can omit to calculate the pairs of field values since the relations between fields are irrelevant for this problem. This is a valid cost function because the lowest cost, -4, is only reached if all fields are 1. Let's add the following condition to our task: Fields <span class="emphasis">a</span> and <span class="emphasis">b</span> can <strong>not</strong> be occupied at the same time.
    {`$$f\\left(a,b,c,d\\right)=-a-b-c-d+4ab$$`}
    If <span class="emphasis">a</span> and <span class="emphasis">b</span> are both 1, even if all fields are occupied for maximum reward, the cost is 0, meaning it's worse than all the other possible solutions. Hence, the best cost achievable here is -3, displaying the correct solution. Another practical strategy in QUBO problems is <i>squaring</i>, for instance for the task "Exactly <ins>two out of four</ins> fields should be occupied":
    {`$$f\\left(a,b,c,d\\right)=\\left(a+b+c+d-2\\right)^2$$`}
    {`$$=a^2+2ab+2ac+2ad-4a+b^2+2bc+2bd-4b+c^2+2cd-4c+d^2-4d+4$$`}
    {`$$=-3a-3b-3c-3d+2ab+2ac+2ad+2bc+2bd+2cd$$`}
    This works because when summing up all fields and subtracting 2, the result is only 0 if exactly two fields are 1. But: If no field or one field is occupied, the result would be negative, giving an even better result. This can be fixed by squaring the equation because squaring a negative number will result in a positive value. The squared field values like <span class="emphasis">a<sup>2</sup></span>, <span class="emphasis">b<sup>2</sup></span>, etc. that result from multiplying the equation out would be illegal (i.e. against the rules of QUBO), but since in the case of binary numbers <span class="emphasis">x<sup>2</sup>=x</span>, they can be replaced with <span class="emphasis">a</span>, <span class="emphasis">b</span>, etc. Also, constants like +4 can be omitted as well, because they just shift all results up or down by the same amount. We can check if our cost function works by testing it with different inputs:
    {`$$f\\left(0, 1, 0, 0\\right)=-3$$`}
    {`$$f\\left(1, 0, 1, 0\\right)=-4$$`}
    {`$$f\\left(0, 1, 1, 1\\right)=-3$$`}
    {`$$f\\left(1, 1, 1, 1\\right)=0$$`}
  </p>
  <p>
    Here are some other examples of QUBO equations:
  </p>
  <ol>
    <li>As many fields as possible should be empty. {`$$f\\left(a,b,c,d\\right)=a+b+c+d$$`}</li>
    <li>There should be <ins>no more than one</ins> field occupied. (i.e.: Exactly zero fields or one field should be occupied.) {`$$f\\left(a,b,c,d\\right)=\\left(a+b+c+d-\\frac{1}{2}\\right)^2=2ab+2ac+2ad+2bc+2bd+2cd$$`}</li>
    <li>In every row and every column, <ins>exactly one</ins> field should be occupied. {`$$f\\left(a,b,c,d\\right)=\\left(a+b-1\\right)^2+\\left(c+d-1\\right)^2+\\left(a+c-1\\right)^2+\\left(c+d-1\\right)^2=-2a-2b-2c-2d+2ab+2ac+2bd+2cd$$`}</li>
  </ol>
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