// /src/routes/login/+page.server.ts
import { redirect } from '@sveltejs/kit';

export const load = async ({ fetch, cookies }) => {
	const sessionid = cookies.get('sessionid');

	if (!sessionid) return {};

	const res = await fetch('http://backend:8000/api/user/', {
		headers: {
			cookie: `sessionid=${sessionid}`
		}
	});

	if (res.ok) {
		// Already logged in — redirect to dashboard
		throw redirect(302, '/dashboard');
	}

	return {};
};
