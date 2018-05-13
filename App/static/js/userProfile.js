$("#editDetailsModal").ready(function(){

	$(".removeResident").ready(function(){
		$('[data-toggle="removeResidentTooptip"]').tooltip();
	});
	
	$(".removeResident").click(function(){
		let resParentDiv = $(this).parent();
		resParentDiv.remove();
	});
});