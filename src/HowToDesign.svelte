<script>

</script>

<div class="title">
  <h2>How to design your own graphs</h2>
</div>
<hr />
<div class="text">
  <p>
    Of course, small problem sizes like this are not really exciting; It's time to take on some major ones! Now that you successfully completed this course, you can have fun experimenting with bigger or even self-designed TSPs. The <strong style="color: #2eb6e8;">Demo</strong> tab on the top of the page provides example code and instructions on how to interact with the D-Wave quantum annealers. Coding is not a requirement in these lessons, but even if you have little experience, just give it a try!
  </p>
  <p>
    If you want to submit your own networks to the quantum annealer, you need to convert them to the Hamiltonian first. The tool <span class="emphasis">Graph to Matrix</span>, which can be accessed in the <strong style="color: #2eb6e8;">Downloads</strong> tab, generates a Hamiltonian from a graph input so you don't have to calculate it by hand.
  </p>
  <ol>
    <li>Draw your vertices on a canvas and click <span class="emphasis">Generate</span> to calculate the edges; the distance in pixels between each vertex represents the cost of the corresponding edge.</li>
    <li>The Hamiltonian is created automatically with the correct scaling. Click <span class="emphasis">Save Hamiltonian...</span> to save it on your computer in the NumPy matrix format.</li>
    <li>Click <span class="emphasis">Save Vertices...</span> to save the layout of your graph; this is needed later for evaluating the results.</li>
  </ol>
  <p>
    If you want to visualize the results, download the tool <span class="emphasis">Path Visualizer</span> that reads the results of the annealer and recreates the corresponding paths. You can browse between the solutions and compare their energy in the debug terminal.
  </p>
  <div align="center"><img width="40%" src="/img/GraphToMatrix.png" alt="A snapshot of the interface of the tool Graph to Matrix"></div>
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
