let notifData = [
		{subject: "Notice 1", date: "28/07/1998", body: "This is notice 1"},
		{subject: "Notice 2", date: "10/08/1998", body: "This is notice 2"},
		{subject: "Notice 3", date: "25/12/1998", body: "This is notice 3"},
		{subject: "Notice 4", date: "28/07/1998", body: "This is notice 1"},
		{subject: "Notice 5", date: "10/08/1998", body: "This is notice 2"},
		{subject: "Notice 6", date: "25/12/1998", body: "This is notice 3"},
		{subject: "Notice 7", date: "28/07/1998", body: "This is notice 1"},
		{subject: "Notice 8", date: "10/08/1998", body: "This is notice 2"},
		{subject: "Notice 9", date: "25/12/1998", body: "This is notice 3"},
		{subject: "Notice 10", date: "28/07/1998", body: "This is notice 1"},
		{subject: "Notice 12", date: "10/08/1998", body: "This is notice 2"},
		{subject: "Notice 13", date: "25/12/1998", body: "This is notice 3"},
		];

function fetchData(){
	//MAKE A AJAX REQUEST AND MAKE THE NOTIFICATION LIST IN THE ABOVE FORMAT
	return notifData;
}

$("#notifBody").ready(function(){

	let notifSub     = $("#notifSub");
	let notifDate    = $("#notifDate");
	let notifContent = $("#notifContent");

	let configureTableElements = function(){
		let currNotifData = fetchData();

		currNotifData.forEach(function(notice, index){
			let subj = $("<td></td>").append(notice.subject);
			let date = $("<td></td>").append(notice.date);

			let row  = $("<tr></tr>").append(subj, date);

			$("#notifBody").append(row);
		});

		notifSub.text(currNotifData[0].subject);
		notifDate.text(currNotifData[0].date);
		notifContent.text(currNotifData[0].body);

		$("#notifBody").children().click(function(event){
			let dataIndex = $(this).index();

			notifSub.text(currNotifData[dataIndex].subject);
			notifDate.text(currNotifData[dataIndex].date);
			notifContent.text(currNotifData[dataIndex].body);
			console.log(dataIndex);
		});
	};

	let clearTable = function(){
		$("#notifBody").children().remove();
	}

	configureTableElements();

	$("#refreshNotif").click(function(){
		clearTable();
		configureTableElements();
	});
});

