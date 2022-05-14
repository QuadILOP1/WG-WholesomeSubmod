init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_pat_WG",
            category=["monika", "misc"],
            prompt="Pat Monika's Head",
            random=False,
            pool=True,
            aff_range=(mas_aff.LOVE, None)
        )
    )

label monika_pat_WG:
    m 5fsbfu "Mmm~ That feels nice."
    m 5hsbfu "Keep patting my head [mas_get_player_nickname()]~"
    m "Mmmmmmm~"
    m 1ekbfu "Maybe you can cuddle me and pat my head next time?"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="cuddle_pat_WG",
            category=["monika", "misc"],
            prompt="Cuddle and Pat the Moni",
            random=False,
            pool=True,
            aff_range=(mas_aff.LOVE, None)
        )
    )

label cuddle_pat_WG:
    m 6hubsa "Mmmm~ Cuddles and pats?~"
    m 6subsd "You'll get a lot more than this when I cross over~"
    m 5tsbfa "I promise."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="suprise_hug_WG",
            category=["monika", "misc"],
            prompt="Suprise hug the Moni",
            random=False,
            pool=True,
            aff_range=(mas_aff.LOVE, None)
        )
    )

label suprise_hug_WG:
    m 6wublo "W-what's wrong [player]?"
    m "Is everything okay?"
    m 5tsbfa "You just wanted to hug me huh~ Cutie~"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="suprise_kiss_WG",
            category=["monika", "misc"],
            prompt="Suprise kiss the Moni",
            random=False,
            pool=True,
            aff_range=(mas_aff.LOVE, None)
        )
    )

label suprise_kiss_WG:
    m 6wublo "*Gasp* W-what was that for?"
    m 2wuo "Giving me a kiss so suddenly."
    m 5tsbfa "Cutie~"
    return