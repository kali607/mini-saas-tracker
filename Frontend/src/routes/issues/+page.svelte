<script>
  import { onMount } from 'svelte';
  import { getIssues } from '$lib/api';

  let issues = [];
  let error = null;

  onMount(async () => {
    try {
      issues = await getIssues();
    } catch (err) {
      error = err.message;
    }
  });
</script>

{#if error}
  <p class="text-red-500">Error: {error}</p>
{:else if issues.length === 0}
  <p>No issues found.</p>
{:else}
  <ul>
    {#each issues as issue}
      <li>
        <strong>{issue.title}</strong> - {issue.description}
      </li>
    {/each}
  </ul>
{/if}
