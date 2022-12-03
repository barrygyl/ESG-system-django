
$(".dark").on('click', function (e) {
	$(".body").addClass("is__dark")
	$(".light").removeClass("is_active")
	$(".dark").addClass("is_active")
	document.getElementById("logo_js").src = "/static/assets/img/logos/Logo_white.svg";
	document.getElementById("logo_js_f").src = "/static/assets/img/logos/Logo_white.svg";

});
$(".light").on('click', function (e) {
	$(".body").removeClass("is__dark")
	$(".light").addClass("is_active")
	$(".dark").removeClass("is_active")
	document.getElementById("logo_js").src = "/static/assets/img/logos/Logo.svg";
	document.getElementById("logo_js_f").src = "/static/assets/img/logos/Logo.svg";
});

// Scroll Animation
(function () {

	gsap.registerPlugin(ScrollTrigger);
	gsap.to(".creators_anim1", {
		x: 500,
		duration: 3,
		scrollTrigger: {
			trigger: ".dribbble_svg",
			scrub: true
		}
	});

	gsap.to(".creators_anim2", {
		x: -500,
		duration: 3,
		scrollTrigger: {
			trigger: ".dribbble_svg",
			scrub: true
		}
	});
	gsap.to(".creators_anim3", {
		x: 500,
		duration: 3,
		scrollTrigger: {
			trigger: ".dribbble_svg",
			scrub: true
		}
	});


}());
