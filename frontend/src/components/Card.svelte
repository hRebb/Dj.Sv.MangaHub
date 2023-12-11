<script lang="ts">
    export let book: {
        id: number,
        title: string,
        author: string,
        rating: string,
        read: boolean,
        genre: { name: string }[],
        classification: { name: string }[],
    }
</script>

<ul class="card-customized custom">
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
</ul>

<style lang="scss">
    @use '../CSS/Customed-classes/Customization/containers.card';

    .custom{
        list-style-type: none;
        width: 200px;
    }
</style>