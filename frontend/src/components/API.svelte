<script lang="ts">
    import { onMount } from 'svelte';
    import Card from './Card.svelte';
    import Filter from './Filter.svelte';

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
    let filteredBooks: Book[] = [];
    let selectedGenre: string = 'All';

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

<span class="filter-list-btn">
    <Filter {books} bind:filteredBooks bind:selectedGenre />
    <br>
</span>

<div class="card-grid">
    {#each books as book}
        <Card book={book} />
    {/each}
</div>

<style lang="scss">
    .filter-list-btn
    {
        display: list-item;
    }

    .card-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 10px;
    }
</style>