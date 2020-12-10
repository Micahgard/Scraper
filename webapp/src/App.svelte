<script>
	export let name;

	function handleKeydown(e){
		console.log(e)
		if (e.keyCode == 13){
			e.preventDefault()
			console.log("Submitted")
		}
	}
</script>

<main>
	<h1>Hello {name}!</h1>
	<p>Visit the <a href="https://svelte.dev/tutorial">Svelte tutorial</a> to learn how to build Svelte apps.</p>
	<p>Enter the site you wish to "crawl":</p>
	<form>
		<input on:submit={(e) => e.preventDefault()} on:keypress={(e) => handleKeydown(e)}/>
	</form>
	
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>