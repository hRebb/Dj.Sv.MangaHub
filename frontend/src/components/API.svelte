<script lang="ts">
    import { onMount } from 'svelte';
    import Card from './Card.svelte';

    type Book = {
        id: number,
        title: string,
        author: string,
        rating: string,
        read: boolean,
        genre: { name: string }[],
        classification: { name: string }[],
    };

    let books: Book[] = [];

    onMount(async () => {
        try {
            const response = await fetch('http://127.0.0.1:8000/api/books/');
            if (response.ok) {
                books = await response.json();
            } else {
                console.log('Error:', response.status);
            }
        } catch (error) {
            console.error('Error fetching books:', error);
        }
    });
</script>

<div>
    {#each books as book}
        <Card book={book} />
    {/each}
</div>