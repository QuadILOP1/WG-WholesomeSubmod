from datetime import date
import calendar

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="p_love_you_most",
            category=["monika", "misc", "romance"],
            prompt="I love you most!",
            random=False,
            pool=True,
            aff_range=(mas_aff.LOVE, None)
        )
    )

label p_love_you_most:
    
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="moni_love_you_most",
            category=["monika", "misc", "romance"],
            prompt="I love you most!",
            random=False,
            pool=True,
            aff_range=(mas_aff.LOVE, None)
        )
    )

label moni_love_you_most:
    
    return