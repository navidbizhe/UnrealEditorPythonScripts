import unreal
import sys
#   this Script can be easily hooked with unreal UI through Execute Console Commad nod of Widget blueprint
blueprintName = "AStreamingBluepritn"
blueprintPath = "/Game/Blueprintzzzz"

createdAssetsCount = int(sys.argv[1])  # argv[0] in the command will be the python script path
createdAssetsName = str(sys.argv[2])
createdAssetsName += '%d'

factory = unreal.BlueprintFactory()

# factory.set_editor_property("ParentClass", unreal.PlayerController)
factory.set_editor_property("parent_class", unreal.Character)
# factory.set_editor_property("parent_class", unreal.GameMode)

# assetTools = unreal.AssetTools <- this is wrong because AssetTools is an inteface

# @unreal.uclass()
# class tools(unreal.AssetTools): <- this is wrong because AssetTools is an inteface
#     pass

# myFile = tools.create_asset(blueprintName, blueprintPath, None, factory) <- this is wrong because AssetTools is an inteface
# myFile = unreal.AssetTools.create_asset(blueprintName, blueprintPath, None, factory) <- this is wrong because AssetTools is an inteface

assetTools = unreal.AssetToolsHelpers.get_asset_tools()

for x in range(createdAssetsCount):
    # myFile = assetTools.create_asset(createdAssetsName % (x), blueprintPath, None, factory)
    myFile = assetTools.create_asset(createdAssetsName % x, blueprintPath, None, factory)
    unreal.EditorAssetLibrary.save_loaded_asset(myFile)
