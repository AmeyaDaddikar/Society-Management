$("#billHistory").ready(function(){

	$("#prevBills").children().click(function(event){
		let date = $(this).children().eq(0).text().trim().split("/");
		console.log($.param({'mm':date[0],'yyyy':date[1]}));
		window.location.href = "/bills?" + $.param({'mm':date[0],'yyyy':date[1]});
	});
});