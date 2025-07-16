// src/lib/api.ts
const API_URL = import.meta.env.VITE_API_URL;

export async function getIssues() {
  const res = await fetch(`${API_URL}/issues/`);
  if (!res.ok) {
    throw new Error('Failed to fetch issues');
  }
  return res.json();
}
