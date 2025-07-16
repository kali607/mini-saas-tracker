<script>
  import { onMount } from 'svelte';
  import Chart from 'chart.js/auto';

  export let chartId = 'my-chart';
  export let chartData;
  export let chartOptions;
  let canvas;

  let chartInstance;

  onMount(() => {
    if (chartInstance) {
      chartInstance.destroy();
    }

    chartInstance = new Chart(canvas, {
      type: 'bar',
      data: chartData,
      options: chartOptions
    });
  });
</script>

<canvas bind:this={canvas} id={chartId}></canvas>
