<script>
  import Link from "../../shared/Link.svelte";
</script>

<div class="title">
  <h2>Closing thoughts</h2>
</div>
<hr />
<div class="text">
  <p>
    With new milestones being achieved every year, quantum computing is a rapidly evolving technology that will have a major impact on our lives. It is currently our most promising solution to the problem of optimization as a whole, which is why further research on quantum algorithms for the Traveling Salesman Problem and other tasks is definitely worthwhile.
  </p>
  <p>
    Nevertheless, it is important to recognize the limitations as well. Until this method can be applied to problems relevant to everyday life and business (&#8764;50-100 cities), much progress needs to be made. However, contrary to its (yet) limited capacity and its error rate, the quantum approach has a major potential to be used in real life, since in industry, in most cases, not necessarily the best but a good solution is needed and the speed with which it is found is much more important than its accuracy. Solving the TSP with quantum annealers therefore represents a great opportunity that can significantly accelerate manufacturing, logistics and research processes in the future.
  </p>
  <h3>Thank you notes</h3>
  <p>
    I would like to sincerely thank everyone who supported me in this research, especially <Link target="https://www.dwavesys.com/">D-Wave Systems Inc.</Link> and the <Link target="https://www.fz-juelich.de/de/ias/jsc">Jülich Supercomputing Centre</Link>.
  </p>
  <p>
    Special thanks go to <strong>Dennis Willsch</strong> and <strong>Kristen Michielsen</strong> at the JSC for their generous support, guidance and coordination.
  </p>
  <p>
    Thanks also to <strong>René Grünbauer</strong> from Gymnasium der Regensburger Domspatzen, who made the project possible through his excellent ideas.
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