<script>
  import Link from "../../shared/Link.svelte";
  import { _ } from "svelte-i18n";
</script>

<div class="title">
  <h2>{$_("lesson-xxxxx.h2-0")}</h2>
</div>
<hr />
<div class="text">
  <p>
    {@html $_("lesson-xxxxx.p-0")}
    {`$$O\\left(n\\right)\\approx n^4$$`}
  </p>
  <div style="float: right; margin: 0 20px"><img width="300" src="/img/Inspector.png" alt="A visualization of the network of qubits on the QPU that are involved in the calculation of a TSP of size 8"></div>
  <p>
    {@html $_("lesson-xxxxx.p-1")}
  </p>
  <p>
    {@html $_("lesson-xxxxx.p-2")}
  </p>
  <h3>{$_("lesson-xxxxx.h3-0")}</h3>
  <p>
    {$_("lesson-xxxxx.p-3")} <Link target="https://docs.ocean.dwavesys.com/en/stable/concepts/embedding.html" newPage={true}>{$_("lesson-xxxxx.Link-0")}</Link>.
  </p>
  <p>
    {$_("lesson-xxxxx.p-4")}
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
