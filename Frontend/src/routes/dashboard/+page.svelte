<script lang="ts">
	export let data;
</script>

<h1 class="text-xl font-bold">Dashboard</h1>

{#if data.user}
	<p>Welcome, {data.user.email}</p>
{:else}
	<p>Not logged in</p>
{/if}
