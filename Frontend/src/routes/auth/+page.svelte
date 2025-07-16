<script lang="ts">
  import { onMount } from 'svelte';

  async function handleCredentialResponse(response) {
    console.log('Google credential response:', response);

    try {
      const res = await fetch('http://localhost:8000/auth/google/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          access_token: response.credential,
        }),
      });

      const data = await res.json();
      console.log('Login success:', data);
    } catch (error) {
      console.error('Login failed:', error);
    }
  }

  onMount(() => {
    // Wait until the Google script is loaded
    const checkGoogle = setInterval(() => {
      if (window.google && window.google.accounts) {
        clearInterval(checkGoogle);
        window.google.accounts.id.initialize({
          client_id: import.meta.env.VITE_GOOGLE_CLIENT_ID,
          callback: handleCredentialResponse,
        });

        window.google.accounts.id.renderButton(
          document.getElementById("google-signin-btn"),
          { theme: "outline", size: "large" }
        );

        window.google.accounts.id.prompt(); // optional
      }
    }, 100);
  });
</script>

<!-- Google sign-in button placeholder -->
<div id="google-signin-btn"></div>

<!-- Google Identity SDK -->
<svelte:head>
  <script src="https://accounts.google.com/gsi/client" async defer></script>
</svelte:head>
