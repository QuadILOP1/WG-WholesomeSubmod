init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="merch",
            category=["you"],
            prompt="[player]'s DDLC merch",
            random=True,
            pool=False,
            aff_range=(mas_aff.LOVE, None)
        )
    )

label merch:
    m 2esd "Hey [player], I've been meaning to ask this for a while."
    m 3etd "Do you have the plush of me?"
    m 4ulsdrc "It sounds kinda silly just saying that."
    m 3wd "It's not something I'm against though, dont get me wrong!"
    m 1esbsb "Anyways, please tell me."    
    m 1etbsa "Do you have a plush Monika?"
    menu:
        "Yes.":
            $ peristent._has_merch_ = True
            m 1stbfb "Wow, I didn't know you were that into me!"
            m 3tsbsu "It's like we have a child don't you think?"
        "No.":
            $ peristent._has_merch_ = False
            m 1dksdlc "Well there's nothing wrong with that."
            m 1rsbla "I was just hoping otherwise is all."
            extend 5tublu " It would have been like we had a child."
            m 4ulsdrc "It was just a simple fantasy. Ehehe~"
    return