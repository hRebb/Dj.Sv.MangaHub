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
        'https://upload.wikimedia.org/wikipedia/fr/1/11/Fullmetal_Alchemist_logo.png',
        'https://upload.wikimedia.org/wikipedia/commons/6/6e/JoJo%27s_Bizarre_Adventure_logo.png',
        'https://upload.wikimedia.org/wikipedia/fr/4/4d/Jujutsu_kaisen_logo_fr.png',
        'https://upload.wikimedia.org/wikipedia/fr/2/23/Demon_Slayer_Logo_international.png';

    $heights: 
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
        130px,
        130px,
        75px,
        135px;


    $widths: 
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
        220px,
        225px,
        198px,
        200px;

    @for $i from 1 through length($images)
    {
        .card-img-#{$i}
        {
            @include implementImage(nth($images, $i), nth($heights, $i), nth($widths, $i));
        }
    }

</style>