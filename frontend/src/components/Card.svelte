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

<ul class="card-customized card-implement card-grid-container">
    <li class="card-img card-img-{book.id}"></li>
    <li class="card-title">{book.title}</li>
    <li class="card-auth">{book.author}</li>
    <li class="card-rate">{book.rating}</li>
    {#if book.read}
        <li class="card-read">Has been read</li>
    {:else}
        <li class="card-read">Not Yet</li>
    {/if}
    <li class="card-genres-list">
        Genres:
        <br> 
        {#each book.genre as genre} 
            <ol class="card-genre">
                {genre.name}
            </ol> 
        {/each}
    </li>
    <li>
        Classification: 
        {#each book.classification as classification} 
            <ol class="card-classification">
                {classification.name}
            </ol> 
        {/each}
    </li>
    <br>
</ul>

<style lang="scss">
    @use '../CSS/Customed-classes/Customization/containers.card';
    @use '../CSS/svelte-components/cards';
    @use '../fonts/fonts.scss';
    
    @mixin implementTitle($title)
    {
        @if ($title == 'Aref')
        {
            font-family: 'Aref Ruqaa Ink', 'Roboto', sans-serif;
        }

        @if ($title == 'Antiqua')
        {
            font-family: 'Glass Antiqua', cursive;
        }

        @if ($title == 'VT')
        {
            font-family: 'VT323', monospace;
        }

        font-size: 20px;
        font-weight: bold;
        color: #000000;
        padding-bottom: 10px;
    };

    .card-grid-container
    {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
        gap: 20px;
    }

    .card-implement
    {
        list-style-type: none;
        text-align: center;
        width: 245px;
        padding-left: 30px;
        background-color: #f9f9f9;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        border-radius: 8px;
    }

    .card-img
    {
        list-style-type: none;
    }

    .card-img-15
    {
        padding-bottom: 25px;
    }

    ol
    {
        display: flex;
    }

    .card-title
    {
        @include implementTitle('Aref');
    }

    .card-auth, .card-read
    {
        font-family: 'Glass Antiqua', cursive;
        font-size: 21px;
    }

    .card-genres-list
    {
        list-style-type: none;
        text-align: center;
    }

    .card-genre
    {
        display: inline;
        padding-left: 10px;

        @include implementTitle('VT');
    }

    .card-classification
    {
        display: block;
        padding-left: 10px;
    }
</style>