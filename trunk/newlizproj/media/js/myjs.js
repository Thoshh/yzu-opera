$(document).ready(function(){
	//$("div[class='cmtBody']").hide();
	$("#header").click(function(){
	// if ( !$("#textanim span").length )
	//	$("#textanim").html(jQuery.map($("#textanim").html().split(""), function(letter){
	//		return "<span>" + letter + "</span>";
	//	}).join(""));
	
	 $("#textanim span").each(function(i, letter){
		setTimeout(function(){
			$(letter).animate({ fontSize: "3em" }, 2000, "elasinout").animate({ fontSize: "1em" }, 2000, "elasinout");
			}, i * 100);
		});
	 });
	
	//$("h3[class^='commenttitle']").click(function(){
		//var filename=$(this).attr("id");
		//cont="#content"+filename.substring(1,filename.length);
		//content="div[id='content"+comment.substring(3,comment.length)+"']";
	//	cont=".cmtBody"
	//	if(!$(cont).attr("visible")){
	//		$(cont).show("slow");
	//	}
	//	if(!$(cont).attr("hidden")){
	//		$(cont).hide();
	//	}
	//}); 
	$("#comments").find(".cmtBody").hide().end().find("h3").click(function()
													{
														var answer = $(this).next();
														if (!answer.is('.visible'))
														//if (!answer.attr("visible"))
														{
															answer.show("slow");
														}
														else
														{
															answer.hide("slow");
														}
													}); 
});

