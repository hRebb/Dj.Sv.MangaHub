<script lang="ts">
    import { onMount } from 'svelte';

    type Book = {
        id: number,
        title: string,
        author: string,
        rating: string,
        read: boolean,
        genre: number[],
        classification: number[],
    };

    type Genre = {
        id: number,
        name: string,
    };

    type Classification = {
        id: number,
        name: string,
    };

    let books: Book[] = [];
    let genres: Genre[] = [];
    let classifications: Classification[] = [];

    onMount(async () => {
        try {
            const [booksResponse, genresResponse, classificationsResponse] = await Promise.all([
                fetch('http://127.0.0.1:8000/api/books/'),
                fetch('http://127.0.0.1:8000/api/genre/'),
                fetch('http://127.0.0.1:8000/api/classifications/')
            ]);

            if (!booksResponse.ok || !genresResponse.ok || !classificationsResponse.ok) {
                console.error('Error fetching data');
                return;
            }

            books = await booksResponse.json();
            genres = await genresResponse.json();
            classifications = await classificationsResponse.json();
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    });
</script>

{#await books}
    <p>Loading...</p>
{:then}
    <ul>
        {#each books as book}
            <li>{book.title}</li>
            <li>{book.author}</li>
            <li>{book.rating}</li>
            {#if book.read}
                <li>Has been read</li>
            {:else}
                <li>Not Yet</li>
            {/if}
            <li>
                Genres: 
                    {#each book.genre as genreId}
                        {genres.find(g => g.id === genreId)?.name}
                    {/each}
            </li>
            <li>
                Classification:
                {#each book.classification as classificationId} 
                    {classifications.find(c => c.id === classificationId)?.name}
                {/each}
            </li>
            <br>
        {/each}
    </ul>
{/await}
