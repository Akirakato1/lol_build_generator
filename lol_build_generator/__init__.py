# __init__.py

# Version of the lol_build_generator package
__version__ = "1.0.0"

import os

def create_word_tuples_list(low, index, remove="Blank"):
    words=list(filter(lambda x: x!="Blank",low))
    for i in range(len(words)):
        words[i]=(words[i],(index, i))
    return words

def create_runes_tuples_list():
    low=create_word_tuples_list(tree, 0)
    for t in tree:
        low.extend(create_word_tuples_list(keystones[t],1))
        for i in range(3):
            low.extend(create_word_tuples_list(runes[t][i],i+2))
    for i in range(3):
        low.extend(create_word_tuples_list(rune_shards[i],-1))
    return low

tree=["Precision","Domination","Sorcery","Resolve","Inspiration"]
keystones={}
runes={}
keystones["Precision"]=["PressTheAttack","LethalTempo","Blank","FleetFootwork","Conqueror"]
keystones["Domination"]=["Electrocute","Predator","Blank","DarkHarvest","HailOfBlades"]
keystones["Sorcery"]=["Blank","SummonAery","ArcaneComet","PhaseRush","Blank"]
keystones["Resolve"]=["Blank","GraspOfTheUndying","Aftershock","Guardian","Blank"]
keystones["Inspiration"]=["Blank","GlacialAugment","UnsealedSpellbook","FirstStrike","Blank"]
runes["Precision"]=[["Blank","Overheal","Triumph","PresenceOfMind","Blank"],
                    ["Blank","LegendAlacrity","LegendTenacity","LegendBloodline","Blank"],
                    ["Blank","CoupDeGrace","CutDown","LastStand","Blank"]]
runes["Domination"]=[["Blank","CheapShot","TasteOfBlood","SuddenImpact","Blank"],
                     ["Blank","ZombieWard","GhostPoro","EyeballCollection","Blank"],
                     ["RavenousHunter","IngeniousHunter","Blank","RelentlessHunter","UltimateHunter"]]
runes["Sorcery"]=[["Blank","NullifyingOrb","ManaflowBand","NimbusCloak","Blank"],
                  ["Blank","Transcendence","Celerity","AbsoluteFocus","Blank"],
                  ["Blank","Scorch","Waterwalking","GatheringStorm","Blank"]]
runes["Resolve"]=[["Blank","Demolish","FontOfLife","ShieldBash","Blank"],
                  ["Blank","Conditioning","SecondWind","BonePlating","Blank"],
                  ["Blank","Overgrowth","Revitalize","Unflinching","Blank"]]
runes["Inspiration"]=[["Blank","HextechFlashtraption","MagicalFootwear","PerfectTiming","Blank"],
                      ["Blank","FuturesMarket","MinionDematerializer","BiscuitDelivery","Blank"],
                      ["Blank","CosmicInsight","ApproachVelocity","TimeWarpTonic","Blank"]]
rune_shards=[["Adaptive", "AttackSpeed","AbilityHaste"],
             ["Adaptive","Armor","MagicResist"],
             ["Health","Armor","MagicResist"]]

directory_rune="../Assets/Runes_Assets/"
directory_item="../Assets/Items_assets/"
directory_summoner="../Assets/Summoners_Spells_Assets/"

runes_low=create_runes_tuples_list()
items=[i[0:-4] for i in os.listdir(directory_item)]
summoners=[i[0:-4] for i in os.listdir(directory_summoner)]
background_color=(102,85,0)

unit=64
boundary_width=5