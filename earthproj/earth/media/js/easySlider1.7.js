/*
 * 	Easy Slider 1.7 - jQuery plugin
 *	written by Alen Grakalic	
 *	http://cssglobe.com/post/4004/easy-slider-15-the-easiest-jquery-plugin-for-sliding
 *
 *	Copyright (c) 2009 Alen Grakalic (http://cssglobe.com)
 *	Dual licensed under the MIT (MIT-LICENSE.txt)
 *	and GPL (GPL-LICENSE.txt) licenses.
 *
 *	Built for jQuery library
 *	http://jquery.com
 *
 */

/*
 * 	Easy Slider 1.7 - jQuery plugin
 *	written by Alen Grakalic	
 *	http://cssglobe.com/post/4004/easy-slider-15-the-easiest-jquery-plugin-for-sliding
 *
 *	Copyright (c) 2009 Alen Grakalic (http://cssglobe.com)
 *	Dual licensed under the MIT (MIT-LICENSE.txt)
 *	and GPL (GPL-LICENSE.txt) licenses.
 *
 *	Built for jQuery library
 *	http://jquery.com
 *
 */
 
/*
 *	markup example for $("#slider").easySlider();
 *	
 * 	<div id="slider">
 *		<ul>
 *			<li><img src="images/01.jpg" alt="" /></li>
 *			<li><img src="images/02.jpg" alt="" /></li>
 *			<li><img src="images/03.jpg" alt="" /></li>
 *			<li><img src="images/04.jpg" alt="" /></li>
 *			<li><img src="images/05.jpg" alt="" /></li>
 *		</ul>
 *	</div>
 *
 */

(function($) {

	$.fn.easySlider = function(options){
	  
		// default configuration properties
		var defaults = {			
			prevId: 		'prevBtn',
			prevText: 		'Previous',
			nextId: 		'nextBtn',	
			nextText: 		'Next',
			controlsShow:	true,
			controlsBefore:	'',
			controlsAfter:	'',	
			controlsFade:	true,
			firstId: 		'firstBtn',
			firstText: 		'First',
			firstShow:		false,
			lastId: 		'lastBtn',	
			lastText: 		'Last',
			lastShow:		false,				
			vertical:		false,
			speed: 			800,
			auto:			false,
			pause:			2000,
			continuous:		false, 
			numeric: 		false,
			numericId: 		'controls'
		}; 
		
		var options = $.extend(defaults, options);  
				
		this.each(function() {  
			var obj = $(this); 				
			var s = $("li", obj).length;
			var w = $("li", obj).width(); 
			var h = $("li", obj).height(); 
			var clickable = true;
			obj.width(w); 
			if (!options.vertical) {
                obj.height(h); 
            } else {
                obj.height(h*10+2);
            }
			obj.css("overflow","hidden");
			var ts = s-1;
			var t = 0;
			$("ul", obj).css('width',s*w);			
			
			if(options.continuous){
				$("ul", obj).prepend($("ul li:last-child", obj).clone().css("margin-left","-"+ w +"px"));
				$("ul", obj).append($("ul li:nth-child(2)", obj).clone());
				$("ul", obj).css('width',(s+1)*w);
			};				
			
			if(!options.vertical) $("li", obj).css('float','left');
								
			if(options.controlsShow){
				var html = options.controlsBefore;				
				if(options.numeric){
					html += '<ol id="'+ options.numericId +'"></ol>';
				} else {
					if(options.firstShow) html += '<span id="'+ options.firstId +'"><a href=\"javascript:void(0);\">'+ options.firstText +'</a></span>';
					html += ' <span id="'+ options.prevId +'"><a href=\"javascript:void(0);\">'+ options.prevText +'</a></span>';
					html += ' <span id="'+ options.nextId +'"><a href=\"javascript:void(0);\">'+ options.nextText +'</a></span>';
					if(options.lastShow) html += ' <span id="'+ options.lastId +'"><a href=\"javascript:void(0);\">'+ options.lastText +'</a></span>';				
				};
				
				html += options.controlsAfter;						
				$(obj).after(html);										
			};
			
			if(options.numeric){									
				for(var i=0;i<s;i++){						
					$(document.createElement("li"))
						.attr('id',options.numericId + (i+1))
						.html('<a rel='+ i +' href=\"javascript:void(0);\">'+ (i+1) +'</a>')
						.appendTo($("#"+ options.numericId))
						.click(function(){							
							animate($("a",$(this)).attr('rel'),true);
						}); 												
				};							
			} else {
				$("a","#"+options.nextId).click(function(){		
					animate("next",true);
				});
				$("a","#"+options.prevId).click(function(){		
					animate("prev",true);				
				});	
				$("a","#"+options.firstId).click(function(){		
					animate("first",true);
				});				
				$("a","#"+options.lastId).click(function(){		
					animate("last",true);				
				});				
			};
			
			function setCurrent(i){
				i = parseInt(i)+1;
				$("li", "#" + options.numericId).removeClass("current");
				$("li#" + options.numericId + i).addClass("current");
			};
			
			function adjust(){
				if(t>ts) t=0;		
				if(t<0) t=ts;	
				if(!options.vertical) {
					$("ul",obj).css("margin-left",(t*w*-1));
				} else {
					//$("ul",obj).css("margin-left",(t*h*-1));
				}
				clickable = true;
				if(options.numeric) setCurrent(t);
			};
			
			function animate(dir,clicked){
				if (clickable){
					clickable = false;
					var ot = t;				
					switch(dir){
						case "next":
							t = (ot>=ts) ? (options.continuous ? t+1 : ts) : t+1;						
							break; 
						case "prev":
							t = (t<=0) ? (options.continuous ? t-1 : 0) : t-1;
							break; 
						case "first":
							t = 0;
							break; 
						case "last":
							t = ts;
							break; 
						default:
							t = dir;
							break; 
					};	
					var diff = Math.abs(ot-t);
					var speed = diff*options.speed;						
					if(!options.vertical) {
						p = (t*w*-1);
						$("ul",obj).animate(
							{ marginLeft: p }, 
							{ queue:false, duration:speed, complete:adjust }
						);				
					} else {
						p = (t*h*-1);
						$("ul",obj).animate(
							{ marginTop: p }, 
							{ queue:false, duration:speed, complete:adjust }
						);					
					};
					
					if(!options.continuous && options.controlsFade){					
						if(t==ts){
							$("a","#"+options.nextId).hide();
							$("a","#"+options.lastId).hide();
						} else {
							$("a","#"+options.nextId).show();
							$("a","#"+options.lastId).show();					
						};
						if(t==0){
							$("a","#"+options.prevId).hide();
							$("a","#"+options.firstId).hide();
						} else {
							$("a","#"+options.prevId).show();
							$("a","#"+options.firstId).show();
						};					
					};				
					
					if(clicked) clearTimeout(timeout);
					if(options.auto && dir=="next" && !clicked){;
						timeout = setTimeout(function(){
							animate("next",false);
						},diff*options.speed+options.pause);
					};
			
				};
				
			};
			// init
			var timeout;
			if(options.auto){;
				timeout = setTimeout(function(){
					animate("next",false);
				},options.pause);
			};		
			
			if(options.numeric) setCurrent(0);
		
			if(!options.continuous && options.controlsFade){					
				$("a","#"+options.prevId).hide();
				$("a","#"+options.firstId).hide();				
			};				
			
		});
	  
	};

})(jQuery);



(function($) {

	$.fn.easySlider1 = function(options){
	  
		var defaults = {			
			speed: 			800,
		}; 
		
		var options = $.extend(defaults, options);  
				
		this.each(function() {  
			var obj = $(this); 				
			var s = $(".post", obj).length;
			var h = $(".post", obj).height(); 
			var clickable = true;
			obj.height(h); 
			obj.css("overflow","hidden");
			var ts = s-1;
			var t = 0;
            
            $("#down").click(function(){		
                animate("next",true);
            });
            $("#up").click(function(){		
                animate("prev",true);				
            });	
            
			function adjust(){
				clickable = true;
			};
			
			function animate(dir,clicked){
				if (clickable){
					clickable = false;
					var ot = t;				
					switch(dir){
						case "next":
							t = (ot>=ts) ? ts : t+1;						
							break; 
						case "prev":
							t = (t<=0) ? 0 : t-1;
							break; 
						case "first":
							t = 0;
							break; 
						case "last":
							t = ts;
							break; 
						default:
							t = dir;
							break; 
					};	
					var diff = Math.abs(ot-t);
					var speed = diff*options.speed;						
                    p = (t*h*-1);
                    $("#inner", obj).animate(
                        { marginTop: p }, 
                        { queue:false, duration:speed, complete:adjust }
                    );					
				};
			};
		});
	};
})(jQuery);



/*
 *  Page Fadein 1.7 - jQuery plugin
 *  written by liz	
 *  markup example for $(".myFade").pageFadeIn();
 *  <div class="myFade">
*	    <div class="OMB">
*           <div class='throbber'><img src='/media/images/throbber.gif' alt='loading' /></div>
*          <span class="back" cp="1" title="上一页"></span>
*          <span class="fore" cp="3" title="下一页"></span>
*       </div>
 *      <ul class="page" pn="5">
 *          <li class="epg"><img src="images/01.jpg" alt="" /></li>
 *          <li class="epg"><img src="images/02.jpg" alt="" /></li>
 *          <li class="epg"><img src="images/03.jpg" alt="" /></li>
 *          <li class="epg"><img src="images/04.jpg" alt="" /></li>
 *          <li class="epg"><img src="images/05.jpg" alt="" /></li>
 *      </ul>
 *  </div>
 *
 */

(function($) {

	$.fn.pageFadeIn = function(options){
	  
		// default configuration properties
		var defaults = {
		}; 
		
		var options = $.extend(defaults, options);  
        
		this.each(function() {  
			var obj = $(this);
            var thrwap = obj.find(".OMB");
            var back = $(".back", thrwap);
            var fore = $(".fore", thrwap);
            var page = $(".page", obj);
            var pn = page.attr("pn");//总页数
            var p = 1;
            try{
                pn = parseInt(pn);
            } catch(e) {
                pn = 1;
            }
			$(".epg:not(:first)", page).hide();
            
            back.click(function(){
                p = back.attr("cp");
                page_click(false);
            });
            fore.click(function(){
                p = fore.attr("cp");
                page_click(true);
            });
            
            function show_throbber(){
                if (!thrwap.find(".throbber").length) {
                    thrwap.prepend("<div class='throbber'><img src='/media/images/throbber.gif' alt='loading' /></div>");
                } else {
                    thrwap.find(".throbber").removeClass("hide");
                }
            }
            function hide_throbber(){
                thrwap.find(".throbber").addClass("hide");
            }
            function show_page(p){
                if (p<1 || p>pn) return;
                $(".epg", page).hide();
                $(".epg:nth-child("+p+")", page).fadeIn();
            }
            function update_bf(isfore){
                if (!isfore) {
                    fore.attr("cp", p+1);
                    show_page(p);
                    p = p - 1;
                    back.attr("cp", p);
                    if (p<1) {
                        back.hide();
                    } else {
                        back.show();
                    }
                    fore.show();
                } else {
                    back.attr("cp", p-1);
                    show_page(p);
                    p = p + 1;
                    fore.attr("cp", p);
                    if (p>pn) {
                        fore.hide();
                    } else {
                        fore.show();
                    }
                    back.show();
                }
            }
            function page_click(isfore){
                show_throbber();
                setTimeout(function(){
                    hide_throbber();
                }, 3000);
                
                p = parseInt(p);
                if (p>pn) return;
                if (p>page.find(".epg").length){
                    /*$j.ajax({
                        url: options.pageUrl,
                        data: {"which": obj.attr("w"), "p": p},
                        beforeSend: function (){
                            show_throbber();
                        },
                        complete: function(req, status){
                            hide_throbber();
                            if ("success" == status){
                                var result = eval('('+req.responseText+')');
                                page.append(result.html);
                                if (p == result.pn) {
                                    update_bf(isfore);
                                }
                            }
                        }
                    });*/
                } else {
                    if (p<1) p = 1;
                    update_bf(isfore);
                }
            }
		});
	};
})(jQuery);


(function($) {
	$.fn.mySlider = function(options){
	  
		// default configuration properties
		var defaults = {
		}; 
		
		var options = $.extend(defaults, options);  
        
		this.each(function() {  
			var obj = $(this);
            var up = $("#up");
            up.hide();
            var down = $("#down");
            var pn = obj.attr("pn");//总post数
            var p = 1;
            try{
                pn = parseInt(pn);
            } catch(e) {
                pn = 1;
            }
			$(".post:not(:first)", obj).hide();
            
            up.click(function(){
                p -= 1;
                if (p<1) return;
                page_click();
                if (p-1<1) {up.hide(); down.show();}
            });
            down.click(function(){
                p += 1;
                if (p>pn) return;
                page_click();
                if (p+1>pn) {down.hide(); up.show();}
            });
            
            function hide_all_comments(){
                $(".extra, .comms").slideUp(function(){
                    $(".comments").removeClass("shcomments");
                });
                $("#content .extra-forms").slideUp();
            }

            function show_page(){
                if (p<1 || p>pn) return;
                $(".post", obj).slideUp();
                $(".post:nth-child("+p+")", obj).slideDown();
            }
            function page_click(isfore){
                hide_all_comments();
                var vp = $("#inner");
                overlay(vp, 0);
                setTimeout(function(){
                    overlay(vp, -1);
                }, 3000);
                if (p>pn || p<1) return;
                if (p>obj.find(".post").length){
                    /*$j.ajax({
                        url: options.pageUrl,
                        data: {"which": obj.attr("w"), "p": p},
                        beforeSend: function (){
                            show_throbber();
                        },
                        complete: function(req, status){
                            hide_throbber();
                            if ("success" == status){
                                var result = eval('('+req.responseText+')');
                                page.append(result.html);
                                if (p == result.pn) {
                                    update_bf(isfore);
                                }
                            }
                        }
                    });*/
                } else {
                    if (p<1) p = 1;
                    show_page();
                }
            }
		});
	};
})(jQuery);

/* myForm */
(function($) {
	$.fn.myForm = function(options){
	  
		var defaults = {
            f: 0,
            onSuccess: null,
            scope: '',
            errorClass: 'error-input',
            errorDiv: '',
            errorMsg: {
                reqString: 'Please fill the required fields',
                reqDate: 'Date is <b>not</b> valid',
                reqNum: 'Only numbers allowed',
                reqMailNotValid: 'E-Mail is <b>not</b> valid',
                reqMailEmpty: 'Please fill e-mail',
                reqSame: 'Repeating inputs are not same',
                reqBoth: 'Related field(s) required',
                reqMin: 'Minimum %1 characters required'
            },
            customErrMsg: '',
            dateSeperator: '.'
		}; 
        /*$.formValidator.validate = function(obj, opts) {
            var valAttr = obj.val();
            var css = opts.errorClass;
            var mail_filter = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
            var numeric_filter = /(^-?\d\d*\.\d*$)|(^-?\d\d*$)|(^-?\.\d\d*$)|(^-?\d*$)/;
            var tmpresult = true;
            var result = true;
            var errorTxt = '';
            if (obj.hasClass('req-string')) {
                tmpresult = (valAttr != '');
                if (!tmpresult) errorTxt = opts.errorMsg.reqString;
                result = result && tmpresult
            }
            if (obj.hasClass('req-same')) {
                tmpresult = true;
                group = obj.attr('rel');
                tmpresult = true;
                $(opts.scope + ' .req-same[rel="' + group + '"]').each(function() {
                    if ($(this).val() != valAttr || valAttr == '') {
                        tmpresult = false
                    }
                });
                if (!tmpresult) {
                    $(opts.scope + ' .req-same[rel="' + group + '"]').parent().parent().addClass('error-same');
                    errorTxt = opts.errorMsg.reqSame
                } else {
                    $(opts.scope + ' .req-same[rel="' + group + '"]').parent().parent().removeClass('error-same')
                }
                result = result && tmpresult
            }
            if (obj.hasClass('req-both')) {
                tmpresult = true;
                if (valAttr != '') {
                    group = obj.attr('rel');
                    $(opts.scope + ' .req-both[rel="' + group + '"]').each(function() {
                        if ($(this).val() == '') {
                            tmpresult = false
                        }
                    });
                    if (!tmpresult) {
                        $(opts.scope + ' .req-both[rel="' + group + '"]').parent().parent().addClass('error-both');
                        errorTxt = opts.errorMsg.reqBoth
                    } else {
                        $(opts.scope + ' .req-both[rel="' + group + '"]').parent().parent().removeClass('error-both')
                    }
                }
                result = result && tmpresult
            }
            if (obj.hasClass('req-email')) {
                tmpresult = mail_filter.test(valAttr);
                if (!tmpresult) errorTxt = (valAttr == '') ? opts.errorMsg.reqMailEmpty: opts.errorMsg.reqMailNotValid;
                result = result && tmpresult
            }
            if (obj.hasClass('req-date')) {
                tmpresult = true;
                var arr = valAttr.split(opts.dateSeperator);
                var curDate = new Date();
                if (valAttr == '') {
                    tmpresult = true
                } else {
                    if (arr.length < 3) {
                        tmpresult = false
                    } else {
                        tmpresult = (arr[0] <= 12) && (arr[1] <= 31) && (arr[2] <= curDate.getFullYear())
                    }
                }
                if (!tmpresult) errorTxt = opts.errorMsg.reqDate;
                result = result && tmpresult
            }
            if (obj.hasClass('req-min')) {
                tmpresult = (valAttr.length >= obj.attr('minlength'));
                if (!tmpresult) errorTxt = opts.errorMsg.reqMin.replace('%1', obj.attr('minlength'));
                result = result && tmpresult
            }
            if (obj.hasClass('req-numeric')) {
                tmpresult = numeric_filter.test(valAttr);
                if (!tmpresult) errorTxt = opts.errorMsg.reqNum;
                result = result && tmpresult
            }
            if (result) {
                obj.removeClass(css)
            } else {
                obj.addClass(css)
            }
            return {
                error: result,
                message: errorTxt
            }
        };*/
        
		var options = $.extend(defaults, options);  
        var canSubmit = false;
        var check_name = function(){
        
        };
        var check_email = function(){
        
        };
        var check_url = function(){
        
        };
        var check_comment = function(){
        
        };
        var show_error = function(msg){
        
        };
        var hide_error = function(){
        
        };
        var error = function(obj){
        
        };
        var ok = function(obj){
        
        };
        this.submit(function(){
            var obj = $(this);
            overlay(obj, options.f);
            setTimeout(function(){
                overlay(obj, -1);
            }, 3000);
            return canSubmit;
        });
	};
})(jQuery);
