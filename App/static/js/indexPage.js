$("#center-paragraph").ready(() => {
	let centreParagraphText = "Society Hub is a state of the art,\ncustomizable social platform for local community groups."

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

$(".fordDIv").ready(()=>{
	let loginDiv  = $("#loginDiv");
	let signupDiv = $("#signupDiv");
	
	loginDiv.css("display","block");
	
	$("#loginButton").click(()=>{
		loginDiv.css("display","block");
		signupDiv.css("display","none");
	});

	$("#signupButton").click(()=>{
		loginDiv.css("display","none");
		signupDiv.css("display","block");
	});

});
