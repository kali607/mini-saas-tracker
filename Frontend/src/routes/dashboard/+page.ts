import { error } from '@sveltejs/kit';

export async function load({ fetch }) {
	try {
		const res = await fetch('http://localhost:8000/api/user/', {
			credentials: 'include'
		});

		const text = await res.text(); // Read raw response first
		console.log('📦 Raw backend response:', text);

		if (!res.ok) {
			throw error(res.status, text);
		}

		const user = JSON.parse(text); // Only parse JSON if status is OK
		return { user };
	} catch (err) {
		console.error('❌ Error loading user in +page.ts:', err);
		throw error(500, 'Internal Error loading user');
	}
}
