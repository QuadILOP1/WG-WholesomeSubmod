init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="merch",
            category=["you"],
            prompt="[player]'s DDLC merch",
            random=True,
            pool=False,
            aff_range=(mas_aff.AFFECTIONATE, None)
        )
    )

label merch:
    m 2esd "Hey [player], I've been meaning to ask this for a while."
    m 3etd "Do you have any merchandise of me?"
    m 4ulsdrc "It sounds kinda silly just saying that."
    m 3wd "It's not something I'm against though, dont get me wrong!"
    m 1esbsb "Anyways, please tell me."
    menu:
        m 1etbsa "Do you have any merch of me?"
        "Yes.":
            $ peristent._has_merch_ = True
            m 1stbfb "Wow, I didn't know you were that into me!"
            

        "No.":
            $ peristent._has_merch_ = False
