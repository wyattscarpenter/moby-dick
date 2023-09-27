# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define i = Character("Ishmael", image="ishmael")
define l = Character("Librarian", image="librarian")
define chapter = Character("",what_text_align=0.5,what_xalign=0.5, what_yalign=0.5)

transform midleft:
    yalign 0.4
    xoffset 10

transform midright:
    yalign 0.4
    xoffset 3150

#I've customized the main menu view to allow jumping to this screen, which seemed more elegant than implementing a new main menu screen for the toc.
label toc: #note that this only works because I've put a bit of code into the default choice screen to make it scroll—otherwise the choices would just irrecoverably progress below the end of the screen! #todo: restyle choices screen to be less bad?
    scene bg room
    menu:
        #"CONTENTS." #if I want to actually display this well, I'll have to fiddle with the styling. But that's true of all the text I guess.
        #TODO: can I somehow get the —s to line up?
        "Etymology":
            jump etymology
        "Extracts":
            jump extracts
        "Chapter I.—Loomings":
            jump c1
        "Chapter II.—The Carpet Bag":
            jump c2
        "cont?":
            jump do_we_cont
        "cont?":
            jump do_we_cont
        "cont?":
            jump do_we_cont
        "cont?":
            jump do_we_cont
        "cont?":
            jump do_we_cont
        "cont?":
            jump do_we_cont
        "cont?":
            jump do_we_cont
        "cont?":
            jump do_we_cont
        "cont?":
            jump do_we_cont
        "cont?":
            jump do_we_cont
        "cont?":
            jump do_we_cont
        "cont?":
            jump do_we_cont
        "cont?":
            jump do_we_cont
        "cont?":
            jump do_we_cont
        "cont?":
            jump do_we_cont
        "cont?":
            jump do_we_cont
        "cont?":
            jump do_we_cont

# The game starts here. The label "start" is a preset, which we preserve for clarity. However, we don't do anything in there, and immediately pass through to the actual first section of the game instead.
#TODO: Inscription page (to nathaniel hawthorne)
label start:
    scene bg room
# typesetting is done with comparisons to the first american edition: https://archive.org/details/mobydickorwhale01melv/
# there's a plain-text copy to work from... I think I may have been using https://www.gutenberg.org/files/2701/2701-h/2701-h.htm so far? Easier than going with, say, ocr. (note to self: should transform this from html to renpy later, possibly programmatically, to catch any italics.)
init python:
    renpy.config.rtl = False #rtl is purposefully off because it was easier to rearrange the two hebrew letters in the book than to mess up the spacing algorithm in that paragraph.

style right_align is text:
    xalign 1.0

label half_title: # "half-title" is the printing jargon for the internal title page. Because we are now into the book proper, we drop the "the RPG" from the name.
    scene bg room
    chapter "{size=+250}MOBY-DICK;\n\n{size=-250}OR{size=+250}\n\nTHE WHALE."

label inscription:
    scene bg room

    #TODO: this isn't formatted in accordance with the book.
    chapter "IN TOKEN\nOF MY ADMIRATION FOR HIS GENIUS \nTHIS BOOK IS INSCRIBED\nTO\nNATHANIEL HAWTHORNE."


label etymology:
    scene bg room

    chapter "ETYMOLOGY.\n{sc}(supplied by a late consumptive usher to a grammar school.){/sc}"

    show librarian at midleft

    "The pale Usher—threadbare in coat, heart, body, and brain; I see him now. He was ever dusting his old lexicons and grammars, with a queer handkerchief, mockingly embellished with all the gay flags of all the known nations of the world. He loved to dust his old grammars; it somehow mildly reminded him of his mortality."

    #todo: rpg tutorial battle
    #todo: you might notice I do some font shenanigans here, and the italic greek still isn't rendered quite right. I will try to hunt down a different century font, I think... #or, failing that, I should make some nice short custom font tags for these
    #todo: actually format the etymologies as a table instead of the handspacing I currently use (and half-assed halfway through)?
    #todo: this is poorly formatted: (missing italics, for example)

    """ “While you take in hand to school others, and to teach them by what name a whale-fish is to be called in our tongue, leaving out, through ignorance, the letter H, which almost alone maketh up the signification of the word, you deliver that which is not true.” —Hackluyt.

“WHALE. * * * Sw. and Dan. hval. This animal is named from roundness or rolling; for in Dan. hvalt is arched or vaulted.” —Webster’s Dictionary.

“WHALE. * * * It is more immediately from the Dut. and Ger. Wallen; A.S. Walw-ian, to roll, to wallow.” —Richardson’s Dictionary.

{space=3}{font=fonts/times.ttf}וח{/font},                        {space=300} Hebrew.\n
{font=fonts/century/CENTURY.ttf}{i}κητος{/i}{/font},   {space=228} Greek.\n
CETUS,                                                 {space=207} Latin.\n
WH{font=fonts/century/CENTURY.ttf}Œ{/font}L,           {space=207} Anglo-Saxon.\n
HVALT,           {space=207} Danish.\n
WAL,           {space=207} Dutch.\n
HWAL,           {space=207} Swedish.\n
HVALUR,           {space=207} Icelandic.\n
WHALE,           {space=207} English.\n
BALEINE,           {space=207} French.\n
BALLENA,           {space=207} Spanish.\n
PEKEE-NUEE-NUEE,           {space=207} Fegee.\n
PEHEE-NUEE-NUEE,           {space=207} Erromangoan."""

label extracts:
    # "({font=fonts/consola.ttf}𝔖𝔲𝔭𝔭𝔩𝔦𝔢𝔡 𝔟𝔶 𝔞 𝔖𝔲𝔟⹀𝔖𝔲𝔟⹀𝔏𝔦𝔟𝔯𝔞𝔯𝔦𝔞𝔫.{/font})" #my current font can't handle this unicode blackletter, so I'm going to have to use an actual blackletter font instead. Or just ignore this styling, the one instance of blackletter in the whole book lol #update: my personal copy of moby dick ignores the font styling. Also, I'm trying to use the font that displays these unicode characters as blackletter in notepad and it still doesn't work in renpy, so maybe it's a renpy problem...
    #"{font=fonts/MonAmourFraktur-Broken.ttf}(Supplied by a Sub-Sub-Librarian){/font}" #if my blackletter font were perfect this would be fine
    chapter "EXTRACTS.\n{font=fonts/MonAmourFraktur-Broken.ttf}({bs}s{/bs}upplied by a {bs}s{/bs}ub={bs}s{/bs}ub=Librarian.){/font}" #This displays properly! # The use of "big smalls" is to make fake capital letters by enlargening lower-case letters, because in this font the actual capitals look bad.
    hide librarian

label c1:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show ishmael at midleft

    # These display lines of dialogue.

    i "Hi it's me the {i}main character (I think? I haven't read Moby----Dick{/i}, before, {b}Ishmael.{/b}"

    hide ishmael

    chapter "CHAPTER I.\n{sc}loomings.{/sc}"

    show ishmael at midleft

    i """Call me Ishmael. Some years ago—never mind how long precisely—having little or no money in my purse, and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world. It is a way I have of driving off the spleen and regulating the circulation. Whenever I find myself growing grim about the mouth; whenever it is a damp, drizzly November in my soul; whenever I find myself involuntarily pausing before coffin warehouses, and bringing up the rear of every funeral I meet; and especially whenever my hypos get such an upper hand of me, that it requires a strong moral principle to prevent me from deliberately stepping into the street, and methodically knocking people’s hats off—then, I account it high time to get to sea as soon as I can. This is my substitute for pistol and ball. With a philosophical flourish Cato throws himself upon his sword; I quietly take to the ship. There is nothing surprising in this. If they but knew it, almost all men in their degree, some time or other, cherish very nearly the same feelings towards the ocean with me.

There now is your insular city of the Manhattoes, belted round by wharves as Indian isles by coral reefs—commerce surrounds it with her surf. Right and left, the streets take you waterward. Its extreme downtown is the battery, where that noble mole is washed by waves, and cooled by breezes, which a few hours previous were out of sight of land. Look at the crowds of water-gazers there.

Circumambulate the city of a dreamy Sabbath afternoon. Go from Corlears Hook to Coenties Slip, and from thence, by Whitehall, northward. What do you see?—Posted like silent sentinels all around the town, stand thousands upon thousands of mortal men fixed in ocean reveries. Some leaning against the spiles; some seated upon the pier-heads; some looking over the bulwarks of ships from China; some high aloft in the rigging, as if striving to get a still better seaward peep. But these are all landsmen; of week days pent up in lath and plaster—tied to counters, nailed to benches, clinched to desks. How then is this? Are the green fields gone? What do they here?

But look! here come more crowds, pacing straight for the water, and seemingly bound for a dive. Strange! Nothing will content them but the extremest limit of the land; loitering under the shady lee of yonder warehouses will not suffice. No. They must get just as nigh the water as they possibly can without falling in. And there they stand—miles of them—leagues. Inlanders all, they come from lanes and alleys, streets and avenues—north, east, south, and west. Yet here they all unite. Tell me, does the magnetic virtue of the needles of the compasses of all those ships attract them thither?

Once more. Say you are in the country; in some high land of lakes. Take almost any path you please, and ten to one it carries you down in a dale, and leaves you there by a pool in the stream. There is magic in it. Let the most absent-minded of men be plunged in his deepest reveries—stand that man on his legs, set his feet a-going, and he will infallibly lead you to water, if water there be in all that region. Should you ever be athirst in the great American desert, try this experiment, if your caravan happen to be supplied with a metaphysical professor. Yes, as every one knows, meditation and water are wedded for ever.

But here is an artist. He desires to paint you the dreamiest, shadiest, quietest, most enchanting bit of romantic landscape in all the valley of the Saco. What is the chief element he employs? There stand his trees, each with a hollow trunk, as if a hermit and a crucifix were within; and here sleeps his meadow, and there sleep his cattle; and up from yonder cottage goes a sleepy smoke. Deep into distant woodlands winds a mazy way, reaching to overlapping spurs of mountains bathed in their hill-side blue. But though the picture lies thus tranced, and though this pine-tree shakes down its sighs like leaves upon this shepherd’s head, yet all were vain, unless the shepherd’s eye were fixed upon the magic stream before him. Go visit the Prairies in June, when for scores on scores of miles you wade knee-deep among Tiger-lilies—what is the one charm wanting?—Water—there is not a drop of water there! Were Niagara but a cataract of sand, would you travel your thousand miles to see it? Why did the poor poet of Tennessee, upon suddenly receiving two handfuls of silver, deliberate whether to buy him a coat, which he sadly needed, or invest his money in a pedestrian trip to Rockaway Beach? Why is almost every robust healthy boy with a robust healthy soul in him, at some time or other crazy to go to sea? Why upon your first voyage as a passenger, did you yourself feel such a mystical vibration, when first told that you and your ship were now out of sight of land? Why did the old Persians hold the sea holy? Why did the Greeks give it a separate deity, and own brother of Jove? Surely all this is not without meaning. And still deeper the meaning of that story of Narcissus, who because he could not grasp the tormenting, mild image he saw in the fountain, plunged into it and was drowned. But that same image, we ourselves see in all rivers and oceans. It is the image of the ungraspable phantom of life; and this is the key to it all.

Now, when I say that I am in the habit of going to sea whenever I begin to grow hazy about the eyes, and begin to be over conscious of my lungs, I do not mean to have it inferred that I ever go to sea as a passenger. For to go as a passenger you must needs have a purse, and a purse is but a rag unless you have something in it. Besides, passengers get sea-sick—grow quarrelsome—don’t sleep of nights—do not enjoy themselves much, as a general thing;—no, I never go as a passenger; nor, though I am something of a salt, do I ever go to sea as a Commodore, or a Captain, or a Cook. I abandon the glory and distinction of such offices to those who like them. For my part, I abominate all honorable respectable toils, trials, and tribulations of every kind whatsoever. It is quite as much as I can do to take care of myself, without taking care of ships, barques, brigs, schooners, and what not. And as for going as cook,—though I confess there is considerable glory in that, a cook being a sort of officer on ship-board—yet, somehow, I never fancied broiling fowls;—though once broiled, judiciously buttered, and judgmatically salted and peppered, there is no one who will speak more respectfully, not to say reverentially, of a broiled fowl than I will. It is out of the idolatrous dotings of the old Egyptians upon broiled ibis and roasted river horse, that you see the mummies of those creatures in their huge bake-houses the pyramids.

No, when I go to sea, I go as a simple sailor, right before the mast, plumb down into the forecastle, aloft there to the royal mast-head. True, they rather order me about some, and make me jump from spar to spar, like a grasshopper in a May meadow. And at first, this sort of thing is unpleasant enough. It touches one’s sense of honor, particularly if you come of an old established family in the land, the Van Rensselaers, or Randolphs, or Hardicanutes. And more than all, if just previous to putting your hand into the tar-pot, you have been lording it as a country schoolmaster, making the tallest boys stand in awe of you. The transition is a keen one, I assure you, from a schoolmaster to a sailor, and requires a strong decoction of Seneca and the Stoics to enable you to grin and bear it. But even this wears off in time.

What of it, if some old hunks of a sea-captain orders me to get a broom and sweep down the decks? What does that indignity amount to, weighed, I mean, in the scales of the New Testament? Do you think the archangel Gabriel thinks anything the less of me, because I promptly and respectfully obey that old hunks in that particular instance? Who ain’t a slave? Tell me that. Well, then, however the old sea-captains may order me about—however they may thump and punch me about, I have the satisfaction of knowing that it is all right; that everybody else is one way or other served in much the same way—either in a physical or metaphysical point of view, that is; and so the universal thump is passed round, and all hands should rub each other’s shoulder-blades, and be content.

Again, I always go to sea as a sailor, because they make a point of paying me for my trouble, whereas they never pay passengers a single penny that I ever heard of. On the contrary, passengers themselves must pay. And there is all the difference in the world between paying and being paid. The act of paying is perhaps the most uncomfortable infliction that the two orchard thieves entailed upon us. But being paid,—what will compare with it? The urbane activity with which a man receives money is really marvellous, considering that we so earnestly believe money to be the root of all earthly ills, and that on no account can a monied man enter heaven. Ah! how cheerfully we consign ourselves to perdition!

Finally, I always go to sea as a sailor, because of the wholesome exercise and pure air of the fore-castle deck. For as in this world, head winds are far more prevalent than winds from astern (that is, if you never violate the Pythagorean maxim), so for the most part the Commodore on the quarter-deck gets his atmosphere at second hand from the sailors on the forecastle. He thinks he breathes it first; but not so. In much the same way do the commonalty lead their leaders in many other things, at the same time that the leaders little suspect it. But wherefore it was that after having repeatedly smelt the sea as a merchant sailor, I should now take it into my head to go on a whaling voyage; this the invisible police officer of the Fates, who has the constant surveillance of me, and secretly dogs me, and influences me in some unaccountable way—he can better answer than any one else. And, doubtless, my going on this whaling voyage, formed part of the grand programme of Providence that was drawn up a long time ago. It came in as a sort of brief interlude and solo between more extensive performances. I take it that this part of the bill must have run something like this:"""

    centered  "“{i}Grand Contested Election for the Presidency of the United States.{/i}{p}\n\n“{sc}whaling voyage by one ishmael.{/sc}{p}\n\n“BLOODY BATTLE IN AFFGHANISTAN.”" #Note that this archaic spelling of Afghanistan is authentic to the original edition.

    i """Though I cannot tell why it was exactly that those stage managers, the Fates, put me down for this shabby part of a whaling voyage, when others were set down for magnificent parts in high tragedies, and short and easy parts in genteel comedies, and jolly parts in farces—though I cannot tell why this was exactly; yet, now that I recall all the circumstances, I think I can see a little into the springs and motives which being cunningly presented to me under various disguises, induced me to set about performing the part I did, besides cajoling me into the delusion that it was a choice resulting from my own unbiased freewill and discriminating judgment.

Chief among these motives was the overwhelming idea of the great whale himself. Such a portentous and mysterious monster roused all my curiosity. Then the wild and distant seas where he rolled his island bulk; the undeliverable, nameless perils of the whale; these, with all the attending marvels of a thousand Patagonian sights and sounds, helped to sway me to my wish. With other men, perhaps, such things would not have been inducements; but as for me, I am tormented with an everlasting itch for things remote. I love to sail forbidden seas, and land on barbarous coasts. Not ignoring what is good, I am quick to perceive a horror, and could still be social with it—would they let me—since it is but well to be on friendly terms with all the inmates of the place one lodges in.

By reason of these things, then, the whaling voyage was welcome; the great flood-gates of the wonder-world swung open, and in the wild conceits that swayed me to my purpose, two and two there floated into my inmost soul, endless processions of the whale, and, mid most of them all, one grand hooded phantom, like a snow hill in the air. 
"""


    # This ends the game.
    #return #if omitted, the game will also end, here at the end.

label new_game_plus:

# CONSUMED Usher... SUB-Librarian (not two subs)
# Ahab: "Stand back, ishmael! I'm beginning to Mōb!"