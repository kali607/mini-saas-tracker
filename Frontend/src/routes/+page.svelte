<script lang="ts">
  import { onMount } from 'svelte';
  import { getIssues } from '$lib/api';

  let issues = [];
  let error: string | null = null;

  onMount(async () => {
    try {
      issues = await getIssues();
    } catch (err) {
      error = 'Failed to load issues';
      console.error(err);
    }
  });
</script>

<h1 class="text-2xl font-bold mb-4">Issue List</h1>

{#if error}
  <p class="text-red-500">{error}</p>
{:else if issues.length === 0}
  <p>No issues found.</p>
{:else}
  <ul class="space-y-2">
    {#each issues as issue}
      <li class="border rounded p-4 shadow-sm">
        <p class="font-semibold">{issue.title}</p>
        <p class="text-sm text-gray-600">{issue.description}</p>
        <p class="text-xs text-gray-500">Severity: {issue.severity}</p>
      </li>
    {/each}
  </ul>
{/if}
