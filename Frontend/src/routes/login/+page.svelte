<script lang="ts">
	import { browser } from '$app/environment';

	let loginUrl = '';

	if (browser) {
		const backendUrl = 'http://localhost:8000'; // ✅ fixed port
		const frontendUrl = window.location.origin;
		loginUrl = `${backendUrl}/accounts/google/login/?next=${frontendUrl}/dashboard`;
	}
</script>

<h1 class="text-2xl font-bold mb-4">Login</h1>

{#if loginUrl}
	<a href={loginUrl}>
		<button class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">
			Login with Google
		</button>
	</a>
{:else}
	<p>Loading login URL…</p>
{/if}
