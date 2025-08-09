<template>
  <div class="app-wrapper">
    <header class="hero">
      <h1>🎓 Medcine acceptance Checker</h1>
      <p>Check your acceptance status by entering your Massar ID</p>
    </header>

    <main class="main-content">
      <div class="search-box">
        <input
          v-model="massarId"
          type="text"
          placeholder="🔍 Enter your Massar ID"
          autocomplete="off"
        />
        <button @click="checkAdmission" :disabled="loading || !massarId.trim()">Check</button>
      </div>

      <div class="message-area">
        <p v-if="loading" class="status loading">⏳ Checking...</p>
        <p v-if="result" class="status success">✅ {{ result }}</p>
        <p v-if="error" class="status error">❌ {{ error }}</p>
      </div>
    </main>

    <footer class="footer">
      Built with passion by Oubay  | © 2025
    </footer>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  data() {
    return {
      massarId: '',
      result: null as string | null,
      error: null as string | null,
      loading: false,
    };
  },
  methods: {
    async checkAdmission() {
      this.result = null;
      this.error = null;
      this.loading = true;

      try {
        const res = await fetch('http://127.0.0.1:5000/api/check', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ massar_id: this.massarId }),
        });
        const data = await res.json();

        if (res.ok) {
          this.result = data.result;
        } else {
          this.error = data.error || 'Unknown error occurred';
        }
      } catch (e) {
        this.error = 'Could not connect to the server';
      } finally {
        this.loading = false;
      }
    },
  },
});
</script>

<style>
body, html {
  margin: 0;
  padding: 0;
  height: 100%;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
  color: #222;
  overflow: hidden;
  position: relative;
}

/* Subtle radial background */
body::before {
  content: "";
  position: fixed;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: radial-gradient(circle at center, rgba(255 255 255 / 0.15), transparent 70%);
  pointer-events: none;
  z-index: 0;
}

.app-wrapper {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  justify-content: center;
  align-items: center;
  padding: 3rem 1.5rem;
  box-sizing: border-box;
  position: relative;
  z-index: 1;
}

.hero {
  text-align: center;
  margin-bottom: 2rem;
  color: #fff;
  text-shadow: 0 2px 6px rgb(0 0 0 / 0.3);
}

.hero h1 {
  font-size: 3rem;
  font-weight: 900;
  letter-spacing: 1.3px;
  margin: 0;
}

.hero p {
  font-size: 1.2rem;
  font-weight: 500;
  opacity: 0.85;
  margin-top: 0.5rem;
}

.main-content {
  width: 100%;
  max-width: 520px;
  background: rgba(255 255 255 / 0.95);
  box-shadow: 0 20px 35px rgba(0, 0, 0, 0.15);
  border-radius: 20px;
  padding: 2.5rem 3rem;
  box-sizing: border-box;
  transition: box-shadow 0.3s ease;
}

.main-content:hover {
  box-shadow: 0 25px 45px rgba(0, 0, 0, 0.25);
}

.search-box {
  display: flex;
  gap: 1rem;
  margin-bottom: 2rem;
}

.search-box input {
  flex: 1;
  padding: 1.3rem 1.5rem;
  font-size: 1.2rem;
  border: 2px solid #4facfe;
  border-radius: 14px;
  font-weight: 600;
  color: #333;
  transition: border-color 0.3s ease, box-shadow 0.3s ease;
  outline-offset: 3px;
  outline-color: #00f2fe;
  box-shadow: 0 6px 10px rgb(79 172 254 / 0.25);
}

.search-box input::placeholder {
  color: #999;
  font-weight: 400;
}

.search-box input:focus {
  border-color: #00f2fe;
  box-shadow: 0 0 14px #00f2fe;
}

.search-box button {
  background: #00f2fe;
  color: white;
  font-size: 1.3rem;
  font-weight: 700;
  padding: 1.3rem 2.5rem;
  border: none;
  border-radius: 14px;
  cursor: pointer;
  box-shadow: 0 6px 14px rgba(0, 242, 254, 0.7);
  transition: background-color 0.3s ease, box-shadow 0.3s ease;
  user-select: none;
}

.search-box button:disabled {
  cursor: not-allowed;
  opacity: 0.45;
  box-shadow: none;
}

.search-box button:hover:not(:disabled) {
  background: #009ec3;
  box-shadow: 0 8px 22px rgba(0, 158, 195, 0.9);
}

.message-area {
  font-size: 1.25rem;
  font-weight: 600;
  text-align: center;
  min-height: 3rem;
  max-width: 100%;
}

.status {
  padding: 1.1rem 2.5rem;
  border-radius: 16px;
  margin: 0 auto;
  box-shadow: 0 4px 12px rgb(0 0 0 / 0.07);
}

.loading {
  background-color: #fefefe;
  color: #555;
  font-style: italic;
  border: 2px solid #4facfe;
}

.success {
  background-color: #d4edda;
  color: #155724;
  border: 2px solid #c3e6cb;
}

.error {
  background-color: #f8d7da;
  color: #721c24;
  border: 2px solid #f5c6cb;
}

.footer {
  margin-top: 3rem;
  padding: 1.2rem 2rem;
  background: rgba(255 255 255 / 0.15);
  color: white;
  text-align: center;
  font-size: 0.9rem;
  font-weight: 500;
  border-top: 1px solid rgba(255 255 255 / 0.25);
  backdrop-filter: blur(10px);
  user-select: none;
  width: 100%;
  max-width: 520px;
  border-radius: 0 0 20px 20px;
}
</style>
