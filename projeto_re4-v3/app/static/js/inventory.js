document.querySelectorAll('.slot').forEach(slot => {
    slot.addEventListener('click', () => {
        const modal = document.getElementById('item-modal');

        // Puxando os dados do slot clicado
        const itemId = slot.dataset.itemId;
        const itemName = slot.dataset.itemName;
        const itemDescription = slot.dataset.itemDescription;
        const itemQuantity = slot.dataset.itemQuantity;

        // Preenchendo o modal com os dados do item
        modal.querySelector('#item-name').innerText = itemName;
        modal.querySelector('#item-description').innerText = itemDescription;
        modal.querySelector('#item-quantity').innerText = `Quantidade: ${itemQuantity}`;
        modal.querySelector('#delete-form').action = `/delete_item/${itemId}`;
        modal.querySelector('#edit-link').href = `/edit_item/${itemId}`;

        // Exibindo o modal
        modal.classList.remove('hidden');
    });
});

document.getElementById('close-modal').addEventListener('click', () => {
    document.getElementById('item-modal').classList.add('hidden');
});