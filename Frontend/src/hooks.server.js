// src/hooks.server.js

export const handle = async ({ event, resolve }) => {
  // TEMP: Skip auth check for now
  // const session = getSessionFromCookies(event.cookies);
  // if (!session?.user) {
  //   throw redirect(302, '/login');
  // }

  return resolve(event);
};
