<script>
  import Link from "../../shared/Link.svelte";
</script>

<div class="title">
  <h2>An introduction to the Traveling Salesman Problem</h2>
</div>
<hr />
<div class="text">
  <p>
    You are the representative of a big company that sends you on a business trip through its main sites. Coincidentally, they are located in the eight largest cities in Germany<sup>1</sup>. You want to save as much time and money as possible, of course. If you start from Berlin, visit each city exactly once, and then return to Berlin, in what order should you visit the cities to keep the trip as short as possible?
  </p>
  <div align="center"><img width="300" src="/img/Map.png" alt="A map of Germany with its eight biggest cities marked: Hamburg, Berlin, Düsseldorf, Leipzig, Köln, Frankfurt, Stuttgart, Munich"></div>
  <p>
    That is the question addressed by the Traveling Salesman Problem. Or, put more generally:
  </p>
  <p style="text-align: center">
    <strong>"Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city exactly once and returns to the origin city?"<sup>2</sup></strong>
  </p>
  <div style="float: right"><img width="270" src="/img/MapLines.png" alt="The same map as above where the cities are connected in a circular path"></div>
  <p>
    In the case of such small tasks, a solution by eye is of course possible: If beelines are taken as the measure of distance, the shortest path would be the one as shown, around the outside. But if you have to visit 20, 50, or even 100 cities, the matter is no longer so simple.
  </p>
  <p>
    The <i>Traveling Salesman Problem</i> (or <i>TSP</i> for short) can be found in numerous real-world applications, such as supply chain design, pipeline renovation, and crystal structure analysis. Accordingly, a fast and reliable solution method is important. The catch: The number of possible paths, calculated with the formula {`$$S(n)=\\frac{(n-1)!}{2}$$`} is immense and growing at a huge pace with each added city. In our 8 cities example, we have <span class="emphasis">2520</span> possibilities to choose from, but with 12 cities, there are already <span class="emphasis">19.958.400</span> different paths. Hence, the problem is NP-hard, basically meaning that an algorithm that finds the exact solution for large inputs in a finite time is likely to be impossible.
  </p>
  <h3>Why a quantum approach?</h3>
  <p>
    The TSP is a good example of an "optimization problem". Since we can't try all solutions without waiting for decades and can't calculate the best one definitively, we try to approximate it as best as we can. It is possible to find the <i>"global" optimum</i>, the shortest path of all, but we can just as well end up at a <i>"local" optimum</i>, one of the many shorter paths. Quantum annealers, a subset of quantum computers, are made for this task because of the physical properties of qubits. Additionally, traditional optimization algorithms are slow, whereas a quantum annealer finds its solution in mere microseconds. In this course, we will explore how the quantum annealers of D-Wave can handle the TSP and whether we can find better solutions than with traditional methods.
  </p>
  <div align="center"><img width="400" src="/img/Optimization.png" alt="A hilly landscape with a marked path from the starting point on a hill to the end point in a valley."></div>
  <p style="text-align: center">
    <i>How can we find the deepest valley when seeing just one point at a time? An example for optimization problems<sup>3</sup></i>
  </p>
</div>
<hr>
<div class="refs">
  <h3>References</h3>
  <ol>
    <li><Link target="https://de.wikipedia.org/wiki/Liste_der_Gro%C3%9Fst%C3%A4dte_in_Deutschland" newPage={true}>https://de.wikipedia.org/wiki/Liste_der_Gro%C3%9Fst%C3%A4dte_in_Deutschland</Link>, accessed: 10.03.2022</li>
    <li><Link target="https://en.wikipedia.org/wiki/Travelling_salesman_problem" newPage={true}>https://en.wikipedia.org/wiki/Travelling_salesman_problem</Link>, accessed: 10.03.2022</li>
    <li>Heena Rijhwani, <i>Optimization</i>, (2020), <Link target="https://medium.com/analytics-vidhya/optimization-acb996a4623c" newPage={true}>https://medium.com/analytics-vidhya/optimization-acb996a4623c</Link>, accessed: 10.03.2022</li>
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
