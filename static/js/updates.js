
const editButtons = document.getElementsByClassName("btn-edit");
const updateText = document.getElementById("id_body");
const updateForm = document.getElementById("updateForm");
const submitButton = document.getElementById("submitButton");


const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
//const deleteModal = (document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let updateId = e.target.getAttribute("update_id");
        console.log(`the update is ${updateId}`);
        //let defectId = e.target.getAttribute("defect_id");
        let updateContent = document.getElementById(`update_${updateId}`).innerText;
        updateText.value = updateContent;
        submitButton.innerText = "Save";
        updateForm.setAttribute("action", `edit_update/${updateId}`);
    });
}

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let updateId = e.target.getAttribute("update_id");
        console.log(`the update is ${updateId}`);
        deleteConfirm.href = `delete_update/${updateId}`;
        deleteModal.show();
    });
}

