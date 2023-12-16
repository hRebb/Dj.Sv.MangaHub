<script lang="ts">
	  import Button from "./Button.svelte";
    import Card from "./Card.svelte";

    import { showCardGrid } from "../utils/visibility";

    export let books: {
      id: number;
      title: string;
      author: string;
      rating: string;
      read: boolean;
      genre: { name: string }[];
      classification: { name: string }[];
    }[];

    export let filteredBooks: typeof books;
    export let selectedGenre: string = 'All';

    let genres: string[] = [
      "Action",
      "Aventure",
      "Historique",
      "Mystère",
      "Policier",
      "Surnaturel",
      "SciFi",
      "Horreur",
      "Drame",
      "Post-Apocalyptique",
      "Dystopie",
      "Fantastique",
      "Comédie",
      "Ecole",
      "Tranche de vie",
      "Cyberpunk",
      "All"
    ];

    let classifications: string[] = [
      "Shonen",
      "Seinen",
      "Shojo",
      "Manwha",
    ];
  
    function filterBooks(genre: string) {
      if (genre === 'All') {
        filteredBooks = books;
      } else {
        filteredBooks = books.filter((book) =>
          book.genre.some((g) => g.name === genre)
        );
      }
      showCardGrid.set(selectedGenre === 'All');
    }
</script>
  
<div class="filter-container">
    <p>
      Filtrer par genre :
    </p>
    <Button {genres} {selectedGenre} {filterBooks} />
  
    <div class="filtered-books">
      {#each filteredBooks as book}
        <Card {book} />
      {/each}
    </div>
</div>
  
<style lang="scss">
    @use '../fonts/fonts';
    p {
      font-family: 'Aref Ruqaa Ink';
    }
    .filter-container {
      margin-top: 20px;
    }

    .filtered-books {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 10px;
    }
</style>  