<script lang="ts">
    import Button from "./Button.svelte";
  
    export let options: string[];
    export let selectedOption: string;
    export let filterBooks: (option: string) => void;
</script>
  
<Button {options} {selectedOption} {filterBooks} />
  