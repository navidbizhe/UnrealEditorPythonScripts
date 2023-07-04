import unreal


@unreal.uclass()
class EditorUtils(unreal.GlobalEditorUtilityBase):
    pass


selectedAssets = EditorUtils().get_selected_assets()

for asset in selectedAssets:
    print(asset.get_name())
    unreal.log_error(asset.get_name())
    unreal.log_warning(asset.get_name())
    unreal.log(asset.get_full_name())
    unreal.log(asset.get_fname())
    unreal.log(asset.get_path_name())
    unreal.log(asset.get_class())
    unreal.log("############################################")