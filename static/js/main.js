const likebtn = document.querySelector('.like');
const unlikebtn = document.querySelector('.unlike');


likebtn.addEventListener("click", function(e){
	console.log("Like Button clicked!")
	const style = e.currentTarget.classList;
	unlikebtn.style.backgroundColor="white";
	likebtn.style.backgroundColor="green";
})
unlikebtn.addEventListener("click", function(e){
	console.log("Unlike Button clicked!")
	const style = e.currentTarget.classList;
	likebtn.style.backgroundColor="white";
	unlikebtn.style.backgroundColor="red";
})