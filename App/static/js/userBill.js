$("#billHistory").ready(function(){

	$("#prevBills").children().click(function(event){
		let date = $(this).children().eq(0).text().trim().split("-");
		console.log($.param({'yyyy':date[0],'mm':date[1], 'dd':date[2]}));
		window.location.href = "/bills?" + $.param({'yyyy':date[0],'mm':date[1], 'dd':date[2]});
	});
});