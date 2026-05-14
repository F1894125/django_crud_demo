function validate_form(event) {
    const title = document.getElementById("title").value;
    const author = document.getElementById("author").value;
    const genre = document.getElementById("genre").value;
    const summary = document.getElementById("summary").value;

    if (title.trim() === "") {
        alert ("Title cannot be empty");
        event.preventDefault();
        return false;
    }

    if (author.trim() === "") {
        alert ("Author's name cannot be empty");
        event.preventDefault();
        return false;
    }

    if (genre.trim() === "") {
        alert ("Genre cannot be empty");
        event.preventDefault();
        return false;
    }

    if (summary.trim() === "") {
        alert ("Summary cannot be empty");
        event.preventDefault();
        return false;
    }
}

document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");
    form.addEventListener("submit", validate_form);
});