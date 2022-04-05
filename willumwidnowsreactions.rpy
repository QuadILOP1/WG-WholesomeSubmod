init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_groove",
            category=["Groove Music"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label WG_wrs_groove:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "What are we listening to today?",
            "Let's listen to some music!",
            "Do you have any lo-fi?"
        ],
        'Window Reactions'
    )

    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_groove')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_vscode",
            category=["Visual Studio Code"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label WG_wrs_vscode:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "What language are you using?",
            "Are you making something for me?",
            "What are you coding, honey?"
        ],
        'Window Reactions'
    )

    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_vscode')
    return