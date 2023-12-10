<script lang="ts">
    import { onMount } from'svelte';

    type book = {
        title: string,
        author: string,
        rating: string
    }

    let books: book[] = [];

    onMount(async () => {
        const response = await fetch('http://127.0.0.1:8000/api/books/');
        if (response.ok) {
            books = await response.json();
        } else {
            console.log('Error:', response.status);
        }
    });
</script>

<ul>
    {#each books as book}
        <li>{book.title}</li>
        <li>{book.author}</li>
        <li>{book.rating}</li>
    {/each}
</ul>