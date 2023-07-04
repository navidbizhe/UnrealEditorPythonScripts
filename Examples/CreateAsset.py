import unreal

blueprintName = "AStreamingBluepritn"
blueprintPath = "/Game/Blueprintzzzz"

factory = unreal.BlueprintFactory()

factory.set_editor_property("ParentClass", unreal.PlayerController)
factory.set_editor_property("parent_class", unreal.PlayerController)
factory.set_editor_property("parent_class", unreal.GameMode)


# assetTools = unreal.AssetTools <- this is wrong because AssetTools is an inteface

# @unreal.uclass()
# class tools(unreal.AssetTools): <- this is wrong because AssetTools is an inteface
#     pass

# myFile = tools.create_asset(blueprintName, blueprintPath, None, factory) <- this is wrong because AssetTools is an inteface
# myFile = unreal.AssetTools.create_asset(blueprintName, blueprintPath, None, factory) <- this is wrong because AssetTools is an inteface

assetTools = unreal.AssetToolsHelpers.get_asset_tools()
myFile = assetTools.create_asset(blueprintName, blueprintPath, None, factory)

unreal.EditorAssetLibrary.save_loaded_asset(myFile)

