# Register the submod
init -990 python:
    store.mas_submod_utils.Submod(
        author="QuadILOP1",
        name="WGsWholesomeSubmod",
        description="Interact with Monika in wholesome ways~",
        version="0.1",
    )
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_pat",
            category=["monika", "misc"],
            prompt="Pat Monika's Head",
            random=False,
            pool=True,
            aff_range=(mas_aff.LOVE, None)
        )
    )

label monika_pat:
    m 5fsbfu "Mmm~ That feels nice."
    m 5hsbfu "Keep patting my head [mas_get_player_nickname()]~"
    m "Mmmmmmm~"
    m 1ekbfu "Maybe you can cuddle me and pat my head next time?"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_peck",
            category=["monika", "misc"],
            prompt="Quickly kiss Monika's cheek",
            random=False,
            pool=True,
            aff_range=(mas_aff.LOVE, None)
        )
    )

label monika_peck:
    m 1wubfb "D-did you just peck my cheek?"
    m 3ttbla "Always keeping me on my toes huh?"
    show m 2gtbla
    pause 0.8
    show m 2mtbla
    pause 0.8
    call monika_kissing_motion(duration=0.5, initial_exp="6hubsa", final_exp="6tkbfu", fade_duration=0.5)
    return



# Register the updater
init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="WGsWholesomeSubmod",
            user_name="QuadILOP1",
            repository_name="WG-WholesomeSubmod"
        )
