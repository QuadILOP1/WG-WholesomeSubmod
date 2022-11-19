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
    m 2wuo "W-wha?"
    m 3efa "Welp, you win today!"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="moni_love_you_most_idea",
            category=["monika", "misc", "romance"],
            prompt="She loves you most!",
            random=True,
            pool=False,
            aff_range=(mas_aff.LOVE, None)
        )
    )

label moni_love_you_most_idea:
    m 1subso "I just had a great idea!"
    m 7tubsu "We could race everyday to see who says 'love you most!' first!"
    m 5tubsb "Doesnt that sound like fun?"
    m 5eua "Well... I was going to start this anyways so you dont have a choice. Ehehe~"
    return

init 5 python:
    addEvent(
    Event(
        persistent.event_database,
        eventlabel="moni_love_you_most",
        category=["monika", "misc", "romance"],
        prompt="She loves you most!",
        random=True,
        pool=False,
        aff_range=(mas_aff.LOVE, None)
        )
    )

label moni_love_you_most:
    m 1sua "Love you most [mas_get_player_nickname()]"
    m 3tfu "I win!"
    return