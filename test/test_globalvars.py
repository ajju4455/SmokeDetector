from globalvars import GlobalVars


def test_globalvars():
    # Changing values in globalvars.py is fine for debugging, but when
    # pushing, there should be made sure that the values are correct.
    assert GlobalVars.charcoal_room_id == "11540"
    assert GlobalVars.meta_tavern_room_id == "89"
    assert GlobalVars.smokeDetector_user_id["11540"] == "120914"
    assert GlobalVars.smokeDetector_user_id["89"] == "266345"
    assert len(GlobalVars.privileged_users["11540"]) > 0
    assert len(GlobalVars.privileged_users["89"]) > 0
    assert GlobalVars.blockedTime == 0
    # The following lists must be empty in globalvars.py, because
    # they will be filled later.
    assert len(GlobalVars.auto_ignored_posts) == 0
    assert len(GlobalVars.ignored_posts) == 0
    assert len(GlobalVars.blacklisted_users) == 0
    assert len(GlobalVars.whitelisted_users) == 0
