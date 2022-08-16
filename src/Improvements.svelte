<script>
  import Link from "../../shared/Link.svelte";
  import { _ } from "svelte-i18n";
</script>

<div class="title">
  <h2>{$_("lesson-xxxxy.h2-0")}</h2>
</div>
<hr />
<div class="text">
  <p>
    {$_("lesson-xxxxy.p-0")}
  </p>
  <p>
    {@html $_("lesson-xxxxy.p-1")}
  </p>
  <div align="center"><img width="250" src="/img/MatrixOptimal.png" alt=""></div>
  <p>
    {@html $_("lesson-xxxxy.p-2")}
  </p>
  <p>
    {@html $_("lesson-xxxxy.p-3")}
  </p>
  <div align="center"><img width="600" src="/img/Graphs.png" alt=""><br><i>{$_("lesson_xxxxy.i-0")}</i></div>
  <p>
    {@html $_("lesson-xxxxy.p-4")}
    {`$$H=\\begin{bmatrix}-2 & 2 & 2 & 2 & 2 & \\infty & 0 & \\infty & \\cdots & 4 \\\\ 0 & -2 & 2 & 2 & \\infty & 2 & \\infty & 0 & \\cdots & 0 \\\\ 0 & 0 & -2 & 2 & 0 & \\infty & 2 & \\infty & \\cdots & 4 \\\\ 0 & 0 & 0 & -2 & \\infty & 0 & \\infty & 2 & \\cdots & 2 \\\\ 0 & 0 & 0 & 0 & -2 & 2 & 2 & 2 & \\cdots & 3.6 \\\\ 0 & 0 & 0 & 0 & 0 & -2 & 2 & 2 & \\cdots & 0 \\\\ 0 & 0 & 0 & 0 & 0 & 0 & -2 & 2 & \\cdots & 3.6 \\\\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & -2 & \\cdots & 2 \\\\ \\vdots & \\vdots & \\vdots & \\vdots & \\vdots & \\vdots & \\vdots & \\vdots & \\ddots & \\vdots \\\\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & \\cdots & -2\\end{bmatrix}\\Rightarrow\\begin{bmatrix}-2 & 2 & 2 & 2 & 2 & 100 & 0 & 100 & \\cdots & 4 \\\\ 0 & -2 & 2 & 2 & 100 & 2 & 100 & 0 & \\cdots & 0 \\\\ 0 & 0 & -2 & 2 & 0 & 100 & 2 & 100 & \\cdots & 4 \\\\ 0 & 0 & 0 & -2 & 100 & 0 & 100 & 2 & \\cdots & 2 \\\\ 0 & 0 & 0 & 0 & -2 & 2 & 2 & 2 & \\cdots & 3.6 \\\\ 0 & 0 & 0 & 0 & 0 & -2 & 2 & 2 & \\cdots & 0 \\\\ 0 & 0 & 0 & 0 & 0 & 0 & -2 & 2 & \\cdots & 3.6 \\\\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & -2 & \\cdots & 2 \\\\ \\vdots & \\vdots & \\vdots & \\vdots & \\vdots & \\vdots & \\vdots & \\vdots & \\ddots & \\vdots \\\\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & \\cdots & -2\\end{bmatrix}$$`}
  </p>
  <p>
    {@html $_("lesson-xxxxy.p-5")}
  </p>
  <div align="center"><img width="200" src="/img/MatrixDirected.png" alt="Excerpt of a Tour Matrix where arrows indicate the connections from node A to C and from node C to A"></div>
  <p>
    {`$$\\Rightarrow f\\left(a,b,...,i,j\\right)=...+3aj+5ib+...$$`}
    {$_("lesson-xxxxy.p-6")}
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
