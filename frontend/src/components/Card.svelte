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
            <ol class="card-genre card-genre-{genre.name.toLowerCase().replace(/\s+/g, '-')}">
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
       $titleMap: (
            'Aref': (
                'font-family': 'Aref Ruqaa Ink, Roboto, sans-serif',
            ),
            'Antiqua': (
                'font-family': 'Glass Antiqua, cursive',
            ),
            'VT': (
                'font-family': 'VT323, monospace',
            ),
            'Nova': (
                'font-family': 'Nova Mono, monospace',
            ),
       );

        @if map-has-key($map: $titleMap, $key: $title)
        {
            $styles: map-get($map: $titleMap, $key: $title);
            @each $key, $value in $styles
            {
                #{$key}: #{$value};
            }
        }

        font-size: 20px;
        font-weight: bold;
        color: #000000;
        padding-bottom: 10px;
    };

    @mixin card-genre-style($bg-color, $hover-color)
    {
        box-shadow: inset 0px -7px 7px 0px darken($bg-color, 20%);
        background: linear-gradient(to bottom, $bg-color 5%, $hover-color 100%);
        background-color: $bg-color;
    }

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
        border-radius: 69px 10px 160px 25px;
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
        margin: 10px 10px 10px 10px;
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

    $genre-colors: (
        "action": red,
        "aventure": rgb(79, 139, 79),
        "historique": crimson,
        "mystère": rgb(92, 21, 92),
        "policier": blue,
        "surnaturel": darkorange,
        "scifi": dodgerblue,
        "horreur": darkred,
        "drame": darkslategray,
        "post-apocalyptique": greenyellow,
        "dystopie": darkmagenta,
        "fantastique": darkorchid,
        "comédie": limegreen,
        "ecole": gold,
        "tranche-de-vie": rgba(247, 182, 126, 0.795),
        "cyberpunk": lightskyblue
    );

    .card-genre
    {
        padding-left: 10px;
        border-radius: 28px;
        border: none;
        display: inline-block;
        cursor: pointer;
        padding: 12px 27px;
        text-decoration: none;
        text-shadow: 0px 1px 0px #263666;

        @include implementTitle('VT');
        @each $genreName, $color in $genre-colors
        {
            &-#{$genreName}
            {
                color: #fff;
                @include card-genre-style($color, lighten($color, 20%));
            }
        }
    }

    .card-classification
    {
        display: block;
        padding-left: 0px;
        padding-bottom: 0px;

        @include implementTitle('Nova');
    }
</style>