<script lang="ts">
	  import GenreFilter from "./GenreFilter.svelte";
    import ClassificationFilter from "./ClassificationFilter.svelte";
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
    export let selectedClassification: string = 'All';

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
      "Manwha"
    ];
  
    function filterBooksByGenre(genre: string) {
      selectedGenre = genre;
      updateFilteredBooks();
    }

    function filterBooksByClassification(classification: string) {
      selectedClassification = classification;
      updateFilteredBooks();
    }

    function updateFilteredBooks() {
      if (selectedGenre === 'All' && selectedClassification === 'All') {
        filteredBooks = books;
      } else {
        filteredBooks = books.filter((book) =>
          (selectedGenre === 'All' || book.genre.some((g) => g.name === selectedGenre)) &&
          (selectedClassification === 'All' || book.classification.some((c) => c.name === selectedClassification))
        );
      }
      showCardGrid.set(selectedGenre === 'All' && selectedClassification === 'All');
    }
</script>
  
<div class="filter-container">
  <p>Filtrer par genre :</p>
  <GenreFilter options={genres} selectedOption={selectedGenre} filterBooks={filterBooksByGenre} />

  <p>Filtrer par thème :</p>
  <ClassificationFilter options={classifications} selectedOption={selectedClassification} filterBooks={filterBooksByClassification} />
  

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
      text-align: center;
      font-weight: bold;
      font-size: 25px;
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