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
        <li class="card-img card-img-{book.id}"></li>
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
                <ol>
                    {classification.name}
                </ol> 
            {/each}
        </li>
        <br>
</ul>

<style lang="scss">
    @use '../CSS/Customed-classes/Customization/containers.card';
    @use '../CSS/Customed-classes/Customization/cards.imgs';

    .custom
    {
        list-style-type: square;
        width: 245px;
        padding-left: 30px;
    }

    .card-img
    {
        list-style-type: none;
    }

    .card-img-15
    {
        padding-bottom: 25px;
    }

</style>