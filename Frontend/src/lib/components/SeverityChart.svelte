<script lang="ts">
  import { onMount } from 'svelte';
  import Chart from 'chart.js/auto';

  export let data = [];

  let canvas: HTMLCanvasElement;

  let chart: Chart | null = null;

  onMount(() => {
    if (chart) chart.destroy();

    const labels = data.map(d => d.severity);
    const counts = data.map(d => d.count);

    chart = new Chart(canvas, {
      type: 'bar',
      data: {
        labels,
        datasets: [
          {
            label: 'Issue Severity',
            data: counts,
            backgroundColor: ['#f87171', '#facc15', '#34d399'],
            borderRadius: 6
          }
        ]
      },
      options: {
        responsive: true,
        plugins: {
          legend: {
            position: 'top'
          }
        }
      }
    });
  });
</script>

<canvas bind:this={canvas} width="400" height="200"></canvas>
