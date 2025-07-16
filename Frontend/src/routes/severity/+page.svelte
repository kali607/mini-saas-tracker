<script>
  import { onMount } from "svelte";
  import Chart from "chart.js/auto";
  let startDate = "";
  let endDate = "";

  let chart;

  async function fetchChartData() {
    const params = new URLSearchParams();
    if (startDate) params.append("start_date", startDate);
    if (endDate) params.append("end_date", endDate);

    const res = await fetch(`http://localhost:8010/api/dashboard/severity-chart/?${params}`);
    const data = await res.json();

    const labels = data.map(d => d.severity);
    const counts = data.map(d => d.count);

    if (chart) chart.destroy();
    const ctx = document.getElementById("chart");
    chart = new Chart(ctx, {
      type: "bar",
      data: {
        labels: labels,
        datasets: [{
          label: "Issue Count",
          data: counts,
          backgroundColor: "#60a5fa",
        }]
      }
    });
  }

  onMount(fetchChartData);
</script>

<h1>Severity Chart</h1>
<div class="filters">
  <label>Start Date: <input type="date" bind:value={startDate} on:change={fetchChartData} /></label>
  <label>End Date: <input type="date" bind:value={endDate} on:change={fetchChartData} /></label>
</div>

<canvas id="chart" width="400" height="200"></canvas>
