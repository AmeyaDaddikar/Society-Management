$("#center-paragraph").ready(() => {
	let centreParagraphText = "Community Hub is a state of the art,\ncustomizable social platform for local community groups."

	let currTextIndex = 0;
	let centreParagraphElement = document.getElementById("center-paragraph");
	let cursor = ["|","|","|","|","|","|","|","|","|","|","","","","","","","","","",""];

	let printCenterText = setInterval(() => {
		if(currTextIndex > centreParagraphText.length){
			setTimeout(()=>{currTextIndex = -1;},2000);
		
		}
		else{
			currTextIndex+= 1;
			centreParagraphElement.innerHTML = centreParagraphText.slice(0, currTextIndex) + cursor[currTextIndex % cursor.length];
		}
	}, 40);
});
