const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const saveButton = document.getElementById('create_service');
const container = document.getElementById('container');


signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});

saveButton.addEventListener('click', () => {
	container.remove();
});