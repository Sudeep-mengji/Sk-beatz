var tl=gsap.timeline()

tl.from(".scrol-left",{
    x:-40,
    duration:1,
    opacity:0,
    scrollTrigger:{
        trigger:".scrol-left",
        scroller:"body",
        start:"top 60%",
        end:"top 45%",
        scrub:2
    }
})

tl.from(".scrol-right",{
    x:40,
    duration:1,
    opacity:0,
    scrollTrigger:{
        trigger:".scrol-right",
        scroller:"body",
        start:"top 60%",
        end:"top 45%",
        scrub:2
    }
})

tl.from(".scrol-up",{
    x:-40,
    duration:0.3,
    opacity:0,
    scrollTrigger:{
        trigger:".scrol-up",
        scroller:"body",
        start:"top 60%",
        end:"top 45%",
        scrub:0.5
    }
})

tl.from(".scrol-round",{
    x:-50,
    duration:0.3,
    opacity:0,
    scrollTrigger:{
        trigger:".scrol-round",
        scroller:"body",
        start:"top 60%",
        end:"top 45%",
        scrub:2
    }
})

tl.from(".scrol-round2",{
    x:-50,
    duration:0.3,
    opacity:0,
    scrollTrigger:{
        trigger:".scrol-round2",
        scroller:"body",
        start:"top 60%",
        end:"top 45%",
        scrub:2
    }
})