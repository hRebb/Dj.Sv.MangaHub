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

    @mixin implementImage($url, $height, $width)
    {
        background-image: url($url);
        height: $height;
        width: $width;
        background-repeat: no-repeat;
        background-size: contain;
    };

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

    $images: 
        'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Vinland_Saga_simplified_logo.svg/langfr-220px-Vinland_Saga_simplified_logo.svg.png', 
        'https://upload.wikimedia.org/wikipedia/fr/b/b2/Death_Note_Logo.svg', 
        'https://upload.wikimedia.org/wikipedia/fr/8/81/Gunnm.png',
        'https://upload.wikimedia.org/wikipedia/commons/f/f1/Berserk_anime_logo.png',
        'https://upload.wikimedia.org/wikipedia/fr/thumb/9/94/Attaque_des_Titans_CMJN.svg/langfr-1920px-Attaque_des_Titans_CMJN.svg.png',
        'https://upload.wikimedia.org/wikipedia/fr/thumb/1/1a/Logo_One_piece.svg/langfr-1920px-Logo_One_piece.svg.png',
        'https://upload.wikimedia.org/wikipedia/fr/thumb/c/c8/Logo_FairyTail.svg/langfr-1920px-Logo_FairyTail.svg.png',
        'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Naruto_logo.svg/langfr-1920px-Naruto_logo.svg.png',
        'https://upload.wikimedia.org/wikipedia/fr/f/f5/Dragon_ball_logo.png',
        'https://upload.wikimedia.org/wikipedia/fr/d/d9/Logo_GTO.png',
        'https://upload.wikimedia.org/wikipedia/fr/thumb/4/45/Logo_Hunter_x_Hunter.svg/langfr-1280px-Logo_Hunter_x_Hunter.svg.png',
        'https://upload.wikimedia.org/wikipedia/fr/1/11/Fullmetal_Alchemist_logo.png';

    $widths: 
        190px, 
        100px, 
        70px,
        110px,
        125px,
        130px,
        105px,
        109px,
        110px,
        145px,
        130px,
        130px;


    $heights: 
        230px, 
        245px, 
        230px,
        235px,
        240px,
        230px,
        225px,
        230px,
        230px,
        225px,
        225px,
        220px;

    @for $i from 1 through length($images)
    {
        .card-img-#{$i}
        {
            @include implementImage(nth($images, $i), nth($widths, $i), nth($heights, $i));
        }
    }

</style>