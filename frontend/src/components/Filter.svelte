<script lang="ts">
	  import Button from "./Button.svelte";
    import Card from "./Card.svelte";

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
      "action",
      "aventure",
      "historique",
      "mystère",
      "policier",
      "surnaturel",
      "scifi",
      "horreur",
      "drame",
      "post-apocalyptique",
      "dystopie",
      "fantastique",
      "comédie",
      "ecole",
      "tranche-de-vie",
      "cyberpunk"
    ];
  
    function filterBooks(genre: string) {
      if (genre === 'All') {
        filteredBooks = books;
      } else {
        filteredBooks = books.filter((book) =>
          book.genre.some((g) => g.name === genre)
        );
      }
    }
</script>
  
<div class="filter-container">
    <Button {genres} {selectedGenre} {filterBooks} />
  
    <div class="filtered-books">
      {#each filteredBooks as book}
        <Card {book} />
      {/each}
    </div>
</div>
  
<style>
    .filter-container {
      margin-top: 20px;
    }
</style>  