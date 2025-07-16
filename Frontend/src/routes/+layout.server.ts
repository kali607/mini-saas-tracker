// /src/routes/+layout.server.ts
import type { LayoutServerLoad } from './$types';
import { redirect } from '@sveltejs/kit';

export const load: LayoutServerLoad = async ({ fetch, cookies, url }) => {
	const sessionid = cookies.get('sessionid');
	const pathname = url.pathname;

	// Skip auth check on public routes
	const publicRoutes = [
		'/login',
		'/accounts',
		'/accounts/google',
		'/accounts/google/login',
		'/accounts/google/login/callback'
	];

	if (publicRoutes.some((route) => pathname.startsWith(route))) {
		return {};
	}

	if (!sessionid) {
		throw redirect(302, '/login');
	}

	try {
		const res = await fetch('http://backend:8000/api/user/', {
			headers: {
				cookie: `sessionid=${sessionid}`
			}
		});

		if (res.ok) {
			const user = await res.json();
			return { user };
		} else {
			// Session invalid or expired
			throw redirect(302, '/login');
		}
	} catch (error) {
		console.error('Error verifying session:', error);
		throw redirect(302, '/login');
	}
};
