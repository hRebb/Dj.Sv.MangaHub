<script lang="ts">
    import { onMount } from 'svelte';

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
            {#each book.genre as genre} 
                <ol>
                    {genre.name}
                </ol> 
            {/each}
        </li>
        <li>
            Classification: 
            {#each book.classification as classification} 
                {classification.name} 
            {/each}
        </li>
        <br>
    {/each}
</ul>