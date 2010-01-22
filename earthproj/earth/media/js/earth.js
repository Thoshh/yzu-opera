var $j = jQuery.noConflict();

jQuery(function($){
    // quick comments
    $j("#collapsible").toggle(function(){
        $j("#respond").slideDown(function(){
            $j("#cancel").click(function(){
                $j("#respond").slideUp().addClass("bhide");
            });
        });
    }, function(){
        $j("#respond").slideUp().removeClass("bhide");
    });
    
    // footinfo
    $j(".greybg .LR").toggle(function(){
        var obj = $j(this);
        var bg = obj.parents(".greybg");
        var bd = bg.next(".greybd");
        
        bg.addClass("FBB");
        bg.children(".GAB,.FAB,.HAB").fadeIn(function(){
            bd.fadeOut();
            obj.removeClass("JS");
            obj.addClass("KS");
            obj.attr("title", "Restore");
        });
    }, function(){
        var obj = $j(this);
        var bg = obj.parents(".greybg");
        var bd = bg.next(".greybd");

        bg.removeClass("FBB");
        bd.fadeIn(function(){
            bg.children(".GAB,.FAB,.HAB").fadeOut();
            obj.removeClass("KS");
            obj.addClass("JS");
            obj.attr("title", "Minimize");
        });
    });

    try{
        $j(".M4").pageFadeIn({
            pageUrl: "/getpage/"
        });
    } catch(e){alert(e)}
    
    // comments
    $j(".bmain .comments").toggle(function(){
        var obj=$j(this);
        obj.parent().nextAll(".extra, .comms").slideDown(function(){
            obj.addClass("shcomments");
            $j(this).removeClass("bhide");
        });
        $j("#content .extra-forms").slideDown(function(){
            $j(this).removeClass("bhide");
        });
    }, function(){
        var obj=$j(this);
        obj.parent().nextAll(".extra, .comms").slideUp(function(){
            obj.removeClass("shcomments");
        });
        $j("#content .extra-forms").slideUp();
    });
    
    try{
        $j("#bcmtform").myForm({
            f: 30
        });
        $j("#qcmtform").myForm({
            f: 20
        });
    }catch(e){alert(e)}
    
    // postbar
    $j("#postbar").height($j("#sidebar").height());
    $j("#postbar").hover(function(){
        $j("#postbarw").removeClass("hide");
    }, function(){
        $j("#postbarw").addClass("hide");
    });
    $j(window).scroll(function(){
        var t = $j("#sidebar").offset().top;
        var d = $j(document).scrollTop();
        if (d>t+$j("#sidebar").height()) return;
        if (d>t){
            $j("#postbar").css('top', d-t+40);
            $j("#postbar").height($j("#sidebar").height()-d+t);
        }
    }); 
    try{
        $j("#inner").mySlider({
            pageUrl: "/getpage/"
        });
        /*$j("#content").easySlider1({
            pageUrl: "/getpage/"
        });*/
    } catch(e) {alert(e)}
    
    var hide_ibar = setTimeout(hideIbar, 5000);
    $j("#ibar").hover(function(){
        clearTimeout(hide_ibar);
        showIbar();
    }, function(){
        hide_ibar = setTimeout(hideIbar, 5000);
    });
});
function hideIbar(){
    $j("#ibar").stop().animate({
        top:"-16px"
        }, "slow");
}
function showIbar(){
    $j("#ibar").stop().animate({
        top:"0px"
        }, "slow");
}
function overlay(obj, f){
    if (f >= 0) {
        var p = obj.parent();
        var w = obj.next(".waiting");
        if (!w.length){
            obj.after('<div class="waiting" class="hide"><img src="/media/images/throbber.gif" alt="waiting" /></div>');
            w = obj.next(".waiting");
        }
        w.width(p.width()+f);
        w.height(p.height()+f);
        w.show(function(){
            $j("img", w).css("top", p.height()/2-8);
            $j("img", w).css("left", p.width()/2-8);
            w.removeClass("hide");
        });
    } else {
        obj.next(".waiting").addClass("hide");
    }
}



// AnythingSlider
function formatText(index, panel) {
 return index + "";
}

$j(document).ready(function() {
     $j("#slider").easySlider({
     	//auto: true,
     	continuous: true 
     });
});

// Form Validation
/*$j(document).ready(function(){
     $j('#submit').formValidator({
         scope: '#contactform',
         errorDiv: '#error-message'
     });
});*/

