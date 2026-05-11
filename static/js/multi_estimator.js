document.addEventListener("DOMContentLoaded", () => {
    const add_rows_button = document.querySelector("#add_rows");
    const membership_function = document.querySelector("#membership_function").value;
    const table_container = document.querySelector("#new_entries_container");

    function create_table(new_entry_count, membership_function) {
        const paragraph = document.createElement("p");
        paragraph.textContent = `Add ${new_entry_count} new entries to the table`;
        table_container.appendChild(paragraph);

        const new_entry_table = document.createElement("table");
        new_entry_table.id = "new_entry_table";

        const thead = document.createElement("thead");
        const header_row = document.createElement("tr");

        let columns = [];
        if (membership_function === "Triangular") {
            columns = ["x", "a", "b", "c"];
        } else if (membership_function === "Trapezoidal") {
            columns = ["x", "a", "b", "c", "d"];
        } else if (membership_function === "Gaussian") {
            columns = ["x", "mu", "sigma"];
        } else {
            console.error("Invalid membership function:", membership_function);
            return;
        }

        columns.forEach((column) => {
            const th = document.createElement("th");
            th.textContent = column;
            header_row.appendChild(th);
        });
        thead.appendChild(header_row);
        new_entry_table.appendChild(thead);


        const tbody = document.createElement("tbody");
        for (let i=0; i<new_entry_count; i++) {
            const body_row = document.createElement("tr");

            columns.forEach((column) => {
                const td = document.createElement("td");
                td.innerHTML = `<input type="text" name="entries[${i}][${column}]" id="${column}_${i}" required>`;
                body_row.appendChild(td);
            });

            tbody.appendChild(body_row);
        }

        new_entry_table.appendChild(tbody);
        table_container.appendChild(new_entry_table);

        const submit_button = document.createElement("button");
        submit_button.type = "submit";
        submit_button.textContent = "Submit All Entries";
        
        table_container.appendChild(submit_button);
    }

    add_rows_button.addEventListener("click", () => {
        const new_entry_count_input = document.getElementById("new_entry_count");
        const new_entry_count = parseInt(new_entry_count_input.value, 10);

        if (!isNaN(new_entry_count) && new_entry_count > 0) {
            new_entry_count_input.readOnly = true;
            table_container.innerHTML = "";
            create_table(new_entry_count, membership_function);
        } else {
            alert("Please enter a valid number of new entries to add.");
        }
    });
});