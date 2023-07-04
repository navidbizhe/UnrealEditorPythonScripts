import unreal
from datetime import datetime
@unreal.uclass()
class AutomationLib(unreal.AutomationLibrary):
    pass

datetimeNowSufix = datetime.now().strftime('%d%m%y%H%M%S')
# AutomationLib.take_high_res_screenshot(1280, 720, "myFancyPictureAtRuntime.png", None, False, False, ComparisonTolerance.LOW, "") <- Possible mistake in forgetting the name space for comparisionTolerance
AutomationLib.take_high_res_screenshot(1280, 720, "myFancyPictureAtRuntime_" + datetimeNowSufix + ".png", None, False, False, unreal.ComparisonTolerance.LOW, "")