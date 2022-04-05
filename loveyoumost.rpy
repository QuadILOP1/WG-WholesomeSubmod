init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="wg_love_you_most",
            category=["monika", "misc", "romance"],
            prompt="I love you most!",
            random=False,
            pool=True,
            aff_range=(mas_aff.LOVE, None)
        )
    )

label wg_love_you_most:
    
    return