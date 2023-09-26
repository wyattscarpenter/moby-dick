# "Smallcaps tag for RenPy." https://gist.github.com/methanoliver/166c18caa224fa15ead6dca95cccbb05
# With modifications by me. (Also WTFPL.)

# Released under the terms of WTFPL public license: Do whatever you please with it.
# Smallcaps tag: {sc}
#
# Usage:
#
# This will be {sc}excellent{/sc}
#
# In some situations, giving an explicit size to the small caps letters
# may be required:
#
# This will be {sc=9}excellent{/sc}
#
# Things that are already uppercase (or don't change upon calling upper()
# on them) pass as is, but lowercase letters go uppercase and get wrapped
# in a {size} tag that reduces them to ~80% of the font size.
#
# This is more or less the same way browsers do "font-variant: small-caps".
# 
# We're working from gui.text_size here to produce the default font size 
# for smallcaps, since a text tag can't know what the font size is at the
# time it works, and must give one explicitly to change it.
# This may not be what you want, but you can override it
# without editing this module by explicitly setting the value of 
# gui.smallcaps_scale in an init <positive number>: block

init:

    define gui.smallcaps_scale = int(gui.text_size - (gui.text_size / 0.8))

init 10 python hide:

    import re

    # Magic: this is a unicode-resistant regexp that splits a string into
    # pieces, some of which are spaces, some are consecutive runs of letters
    # which already are capitals or count as capitals, and some are everything
    # else.
    #
    # It's not perfect, since it will miss some more exotic punctuation,
    # but should work for most languages.

    CAPITALS = re.compile(
        r"""([""" +
        r"""!"#%&',/0-9:;<=>@\^\$\(\)\*\+\-\.\?\{\}\|""" +
        r"".join([
            chr(i) for i in xrange(sys.maxunicode)
            if chr(i).isupper()]) +
        r"""]+|[ ]+)"""
    )

    def smallcaps_tag(tag, arg, text, use_smalls_hack=False):

        try:
            arg = int(arg)
        except ValueError:
            arg = None

        result = []
        for element in text:
            if element[0] == renpy.TEXT_TEXT:
                tokens = [x for x in re.split(CAPITALS, element[1]) if x]
                processed = u""
                for token in tokens:
                    # We don't touch what is already uppercase or spaces.
                    if token.upper() == token:
                        processed += token
                    else:
                        # We found a run of lowercase,
                        # so pack up the string we want to keep unchanged,
                        # and wrap this run in size tags.
                        if processed:
                            result += [(renpy.TEXT_TEXT, processed)]
                            processed = u""
                        result += [
                            (renpy.TEXT_TAG,
                            u"size={}".format(arg or gui.smallcaps_scale)),
                            (renpy.TEXT_TEXT, token.upper() if not use_smalls_hack else token),
                            (renpy.TEXT_TAG, u"/size")
                        ]
                # If any tail remained, pack that up too.
                if processed:
                    result += [(renpy.TEXT_TEXT, processed)]
            else:
                result.append(element)
        return result
    def bigsmalls_tag(tag, arg, text): return smallcaps_tag(tag, int(gui.text_size*1.4), text, use_smalls_hack=True)
    config.custom_text_tags["sc"] = smallcaps_tag
    config.custom_text_tags["bs"] = bigsmalls_tag
