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