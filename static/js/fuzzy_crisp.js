document.addEventListener("DOMContentLoaded", () => {
    const add_rows_button = document.getElementById("add_rows");
    const new_entries_container = document.getElementById("new_entries_container");

    function create_table(new_entry_count) {
        const paragraph = document.createElement("p");
        paragraph.textContent = `Add ${new_entry_count} Entries and Membership Values`;
        new_entries_container.appendChild(paragraph);

        const new_entry_table = document.createElement("table");
        new_entry_table.id = "new_entry_table";

        let columns = ["element", "membership"];
        const tbody = document.createElement("tbody");
        for (let i=0; i<new_entry_count; i++) {
            const body_row = document.createElement("tr");

            columns.forEach((column) => {
                const td = document.createElement("td");
                if (column == "element") {
                    td.innerHTML = `<input type="text" name="${column}_${i}" id="${column}_${i}" placeholder="${column} ${i+1}" required>`;
                } else {
                    td.innerHTML = `<input type="text" name="${column}_${i}" id="${column}_${i}" placeholder="${column} (0 to 1)" required>`;
                }

                body_row.appendChild(td);
            });

            tbody.appendChild(body_row);
        }

        new_entry_table.appendChild(tbody);
        new_entries_container.appendChild(new_entry_table);

        const submit_button = document.createElement("button");
        submit_button.textContent = "Submit All Entries";
        submit_button.type = "submit";

        new_entries_container.appendChild(submit_button);
    }

    add_rows_button.addEventListener("click", () => {
        const new_entry_count_input = document.getElementById("new_entry_count");
        const new_entry_count = parseInt(new_entry_count_input.value, 10);

        if (!isNaN(new_entry_count) && new_entry_count > 0) {
            new_entry_count_input.readOnly = true;
            new_entries_container.innerHTML = "";
            create_table(new_entry_count);
        } else {
            alert("Please enter a valid number of new entries to add.");
        }
    });
});