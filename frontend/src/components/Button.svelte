<script lang="ts">
  export let options: string[];
  export let selectedOption: string;
  export let filterBooks: (option: string) => void;

  function handleFilter(option: string) {
    filterBooks(option);
  }
</script>

<div class="filter-buttons">
  {#each options as option}
    <button
      class="btn"
      on:click={() => handleFilter(option)}
      class:active={selectedOption === option}
    >
      {option}
    </button>
  {/each}
</div>

<style lang="scss">
  @mixin buttonStyle($bg-color, $hover-color) {
    box-shadow: inset 0px -7px 7px 0px darken($bg-color, 20%);
    background: linear-gradient(to bottom, $bg-color 5%, $hover-color 100%);
    background-color: $bg-color;
  }

  %template-btn {
    border-radius: 28px;
    border: none;
    display: inline-block;
    cursor: pointer;
    color: #ffffff;
    padding: 12px 27px;
    text-decoration: none;
    text-shadow: 0px 1px 0px #263666;
  }

  .btn {
    @extend %template-btn;
    @include buttonStyle(#2dabf9, #0688fa);

    margin: 10px 10px 10px 10px;

    &:hover {
      @include buttonStyle(#0688fa, #2dabf9);
      background-color: #0688fa;
    }
    &:active {
      position: relative;
      top: 1px;
    }
  }

  .filter-buttons {
    margin-bottom: 20px;
    text-align: center;
  }
</style>  