#pip install -i https://test.pypi.org/simple/ lol-build-generator==1.0.2
#https://test.pypi.org/project/lol-build-generator/1.0.2/

from lol_build_generator import generator as g
g.get_rune_sequence_guide().show()

g.generate_rune_page("102202502000").show()

test_rune_string="dominate, electroctue, sudden impact, eyeball collection, raveenous hunteress, sorcery, transendence, gathering storms, adaptiving, adaptive, health"
rune_test_page=g.generate_rune_page(g.find_closest_runes(test_rune_string))
rune_test_page.show()

test_item_string="ludens tempest, void staff, zhonya's hourglass, rabadon deathcap, dorans blade, refillable potion"
item_test_page=g.generate_item_page(g.find_closest_items(test_item_string))
item_test_page.show()

test_summoner_string="exahust, ghost"
sum_test_page=g.generate_summoner_page(g.find_closest_summoners(test_summoner_string))
sum_test_page.show()a