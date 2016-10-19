if ((navigator.userAgent.indexOf('iPhone') != -1) ||(screen.width <=699) || (navigator.userAgent.indexOf('iPod') != -1) || (navigator.userAgent.indexOf('iPad') != -1)) {
  document.getElementById("muctr").style.visibility = "visible";
}

function closePlay(){
  soundManager.play('nyan');
  $('div.muctr').hide();
}

// Changes the language using language values provided

function changeLanguage(language){
    var values = languages[language];
    for (var key in values) {
         document.getElementById(key).innerHTML = values[key];
    }
    document.getElementById('flav').src = '/images/languages/' + language + '/button.png';
}

// Big chunk of scary JS

var paid = 0;$(window).keypress(function (e) {
    if (e.keyCode == 115) {
        showMenu();
    }
});
$("#showr").click(function () {
    $("#flavors").show("fast", function () {
        $(this).next("div").show("fast", arguments.callee);
    });
});
$("#hidr").click(function () {
    $("#flavors").hide(2000);
});

function getValue(NameOfValue) {
    if (document.cookie.length > 0) {
        begin = document.cookie.indexOf(NameOfValue + "=");
        if (begin != -1) {
            begin += NameOfValue.length + 1;
            end = document.cookie.indexOf(";", begin);
            if (end == -1) end = document.cookie.length;
            return unescape(document.cookie.substring(begin, end));
        }
    }
    return null;
}

function setValue(NameOfValue, value, expiredays) {
    var ExpireDate = new Date();
    ExpireDate.setTime(ExpireDate.getTime() + (expiredays * 24 * 3600 * 1000));
    document.cookie = NameOfValue + "=" + escape(value) + ((expiredays == null) ? "" : "; expires=" + ExpireDate.toGMTString());
}

function remValue(NameOfValue) {
    if (getValue(NameOfValue)) {
        document.cookie = NameOfValue + "=" +
            "; expires=Thu, 01-Jan-70 00:00:01 GMT";
    }
}

function animateStars() {
    $('.star').each(function () {
        thisFrame = $(this).attr('class');
        thisFrame = thisFrame.split(' ');
        thisFrame = thisFrame[1].split('-');
        thisFrame = parseInt(thisFrame[1]);
        if (thisFrame == 6) {
            //6
            $(this).remove();
        } else {
            $(this).removeClass("frame-" + String(thisFrame)).addClass("frame-" + String(parseInt(thisFrame) + 1));
        }
    })
} //400
animateStarsTimer = setInterval(animateStars, 60);

function toast() {
    window.location = "toaster.php"
}

function placeStar() {
    var newStar = $("<div class='star frame-1'><div class='wrapper'><div class='dot dot-1'></div><div class='dot dot-2'></div><div class='dot dot-3'></div><div class='dot dot-4'></div><div class='dot dot-5'></div><div class='dot dot-6'></div><div class='dot dot-7'></div><div class='dot dot-8'></div><div class='dot dot-9'></div></div></div>");
    newStar.css({ //1600
        top: Math.floor(Math.random() * 1200),
        left: Math.floor(Math.random() * 2000)
    }); //1200

    $('body').append(newStar);
} //100
placeStarTimer = setInterval(placeStar, 20);

function animateRainbow() {
    $('.rainbows').toggleClass("shift")
}
animateRainbowTimer = setInterval(animateRainbow, 300);
var startTime = new Date;
var currentTime = new Date;
var seconds;

function timeOnSite() {
    currentTime = new Date;
    seconds = parseFloat((currentTime - startTime) / 1000).toFixed(1);
    $("#timer .seconds").text(seconds);
    if (seconds == "1000.0") {
        pushThousnyan();
    } /* 1000 Seconds */
    if (seconds == "9001.0") {
        nyanThousand();
    } /* 9001 Seconds */
    if (seconds == "100000.0") {
        oneHundred();
    } /* 100,000 Seconds */
    if (seconds == "500000.0") {
        fiveHundred();
    } /* 500,000 Seconds */
    if (seconds == "1000000.0") {
        oneMillinyan();
    } /* 1,000,000 Seconds */
    if (seconds == "5000000.0") {
        fiveMillinyan();
    } /* 5,000,000 Seconds */
}
setTimeOnSite = setInterval(timeOnSite, 100);
/*
function timeTilDeath() {
	now      = new Date();
	kickoff  = Date.parse("December 21, 2012 00:00:00");
	diff = kickoff - now;

	days  = Math.floor( diff / (1000*60*60*24) );
	hours = Math.floor( diff / (1000*60*60) );
	mins  = Math.floor( diff / (1000*60) );
	secs  = Math.floor( diff / 1000 );

	dd = days;
	hh = hours - days  * 24;
	mm = mins  - hours * 60;
	ss = secs  - mins  * 60;

        document.getElementById("doomtime").innerHTML =dd + ' Days  ' +hh + ' Hours ' +mm + ' Minutes ' +ss + ' seconds';
}
setTimeTilDeath = setInterval(timeTilDeath, 100);
*/

function load404(){
checkViews();
pushMissingnyan();
}

var ach_1 = eval(getValue('ach_1'));
var ach_2 = eval(getValue('ach_2'));
var ach_3 = eval(getValue('ach_3'));
var ach_4 = eval(getValue('ach_4'));
var ach_5 = eval(getValue('ach_5'));
var ach_6 = eval(getValue('ach_6'));
var ach_7 = eval(getValue('ach_7'));
var ach_8 = eval(getValue('ach_8'));
var ach_9 = eval(getValue('ach_9'));
var ach_10 = eval(getValue('ach_10'));

function pushThousnyan() {
    if (!ach_1) {
        $('div.ach1').toggle();
        setValue('ach_1', '1337', 365);
    }
}

function nyanThousand() {
    if (!ach_2) {
        $('div.ach2').toggle();
        setValue('ach_2', '1337', 365);
    }
}

function oneHundred() {
    if (!ach_3) {
        $('div.ach3').toggle();
        setValue('ach_3', '1337', 365);
    }
}

function fiveHundred() {
    if (!ach_4) {
        $('div.ach4').toggle();
        setValue('ach_4', '1337', 365);
    }
}

function oneMillinyan() {
    if (!ach_5) {
        $('div.ach5').toggle();
        setValue('ach_5', '1337', 365);
    }
}

function fiveMillinyan() {
    if (!ach_6) {
        $('div.ach6').toggle();
        setValue('ach_6', '1337', 365);
    }
}

function pushMissingnyan() {
    if (!ach_7) {
        $('div.ach7').toggle();
        setValue('ach_7', '1337', 365);
    }
}

function pushRainyan() {
    if (!ach_8) {
        $('div.ach8').toggle();
        setValue('ach_8', '1337', 365);
    }
}

function pushNyanfan() {
    if (!ach_9) {
        $('div.ach9').toggle();
        setValue('ach_9', '1337', 365);
    }
}

function pushObsessed() {
    if (!ach_10) {
        $('div.ach10').toggle();
        setValue('ach_10', '1337', 365);
    }
}

$(document).ready(function () {
    $('div.view').hide();
    $('div.view').height(80)
    $('div.view').width(80)
    $('div.slide').toggle(function () {
        $(this).siblings('div.view').fadeIn('slow');
    }, function () {
        $(this).siblings('div.view').fadeOut('fast');
        return false;
    });
});



$(document).ready(function () {
    $('div.ach1').hide();
    $('div.ach1').toggle(function () {
        $(this).siblings('div.ach1').fadeIn('slow');
    }, function () {
        $(this).siblings('div.ach1').fadeOut('fast');
        return false;
    });
});
$(document).ready(function () {
    $('div.ach2').hide();
    $('div.ach2').toggle(function () {
        $(this).siblings('div.ach2').fadeIn('slow');
    }, function () {
        $(this).siblings('div.ach2').fadeOut('fast');
        return false;
    });
});
$(document).ready(function () {
    $('div.ach3').hide();
    $('div.ach3').toggle(function () {
        $(this).siblings('div.ach3').fadeIn('slow');
    }, function () {
        $(this).siblings('div.ach3').fadeOut('fast');
        return false;
    });
});
$(document).ready(function () {
    $('div.ach4').hide();
    $('div.ach4').toggle(function () {
        $(this).siblings('div.ach4').fadeIn('slow');
    }, function () {
        $(this).siblings('div.ach4').fadeOut('fast');
        return false;
    });
});
$(document).ready(function () {
    $('div.ach5').hide();
    $('div.ach5').toggle(function () {
        $(this).siblings('div.ach5').fadeIn('slow');
    }, function () {
        $(this).siblings('div.ach5').fadeOut('fast');
        return false;
    });
});
$(document).ready(function () {
    $('div.ach6').hide();
    $('div.ach6').toggle(function () {
        $(this).siblings('div.ach6').fadeIn('slow');
    }, function () {
        $(this).siblings('div.ach6').fadeOut('fast');
        return false;
    });
});
$(document).ready(function () {
    $('div.ach7').hide();
    $('div.ach7').toggle(function () {
        $(this).siblings('div.ach7').fadeIn('slow');
    }, function () {
        $(this).siblings('div.ach7').fadeOut('fast');
        return false;
    });
});
$(document).ready(function () {
    $('div.ach8').hide();
    $('div.ach8').toggle(function () {
        $(this).siblings('div.ach8').fadeIn('slow');
    }, function () {
        $(this).siblings('div.ach8').fadeOut('fast');
        return false;
    });
});
$(document).ready(function () {
    $('div.ach9').hide();
    $('div.ach9').toggle(function () {
        $(this).siblings('div.ach9').fadeIn('slow');
    }, function () {
        $(this).siblings('div.ach9').fadeOut('fast');
        return false;
    });
});
$(document).ready(function () {
    $('div.ach10').hide();
    $('div.ach10').toggle(function () {
        $(this).siblings('div.ach10').fadeIn('slow');
    }, function () {
        $(this).siblings('div.ach10').fadeOut('fast');
        return false;
    });
});

$(document).ready(function () {
    $('div.view2').hide();
    $('div.slide2').toggle(function helpMe() {
        $(this).siblings('div.view2').fadeIn('slow');
    }, function () {
        $(this).siblings('div.view2').fadeOut('fast');
        return false;
    });
});

function popitup(url) {
    newwindow = window.open(url, 'Credits', 'height=600,width=800');
    if (window.focus) {
        newwindow.focus()
    }
    return false;
}

function popitup(url) {
    newwindow = window.open(url, 'Store', 'height=600,width=800');
    if (window.focus) {
        newwindow.focus()
    }
    return false;
}

function popitup500(url) {
    newwindow = window.open(url, 'Store', 'height=500,width=500');
    if (window.focus) {
        newwindow.focus()
    }
    return false;
}
       startVolume = 50
        if (document.location.hostname == "localhost") {
          startVolume = 0
        }

function preReq() {
    var deflang = getValue('deflang');

    if (!(deflang in languages)) {
    	deflang = 'eng';
    	setValue('language', 'eng', 365);
	}

	changeLanguage(deflang);
	checkViews();
}

// more inline JS

function showMenu() {
  $("#flavors").show("fast")
;}

function hideMenu() {
  $("#flavors").hide(2000)
;}


if( /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) ) {
 	document.getElementById("muctr").style.visibility = "visible";
}

function blowUpBackground() {

  var hyperColors = ["#0f4d8f", "#0f8f2a", "#8f5a0f", "#8f0f0f", "#840f8f"]

  $("body").css("background-color", hyperColors[Math.floor(Math.random()*hyperColors.length)])

}

var currentVolume = 50;

function volumeDown() {
  currentVolume = currentVolume + 15
  if (currentVolume >= 150) {
    soundManager.setVolume('nyan',200);
    var setSiteOnFire = setInterval( blowUpBackground, 150);
    $("#volume").hide();
    _gaq.push(['_trackEvent', 'Background Blew', seconds]);
  } else {
    soundManager.setVolume('nyan',currentVolume);
  }
}

$("#volume").click(function() {
  _gaq.push(['_trackEvent', 'Lower Volume', currentVolume]);
  if (currentVolume == 95) {
    $(this).text("OMG!!!!!!")
  } else if (currentVolume == 110) {
    $(this).text("OMG!!!!!!!!!!!!!!")
  } else if (currentVolume == 125) {
    $(this).text("OMG!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
  }
  volumeDown();
})

// Might re-introduce this if I can find the old code for it. Remind me.
function lala() {
  if($.Storage.get("troubadourMode") == "1") {
    $("body").append('<div class="troubadour-button">Enable Nyanaoke Mode</div>')
    $(".troubadour-button").click(function() {
      $(this).hide()
      troubadourMode()
    })
  }
}
