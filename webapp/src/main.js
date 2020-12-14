import App from './App.svelte';

const app = new App({
	target: document.body,
	props: {
		name: 'Crawl A Site'
	}
});

export default app;