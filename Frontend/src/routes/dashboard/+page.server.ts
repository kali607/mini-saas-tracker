import { redirect } from '@sveltejs/kit';

export async function load({ fetch }) {
	const res = await fetch(`${import.meta.env.VITE_API_URL}/user/`, {
		credentials: 'include'
	});

	if (!res.ok) {
		throw redirect(302, '/login');
	}

	const user = await res.json();
	return { user };
}
