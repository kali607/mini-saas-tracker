<script>
  import { Bar } from 'svelte-chartjs';
  import {
    Chart as ChartJS,
    Title,
    Tooltip,
    Legend,
    BarElement,
    CategoryScale,
    LinearScale
  } from 'chart.js';

  ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale);

  export let labels = [];
  export let data = [];
  
  const chartData = {
    labels,
    datasets: [
      {
        label: 'Issues by Status',
        data,
        backgroundColor: ['#1f77b4', '#ff7f0e', '#2ca02c'], // colors for bars
      }
    ]
  };

  const chartOptions = {
    responsive: true,
    plugins: {
      legend: { position: 'top' },
      title: { display: true, text: 'Issue Statistics' }
    }
  };
</script>

<Bar data={chartData} options={chartOptions} />
