Set oShell = CreateObject("WScript.Shell")
Set oEnv = oShell.Environment("USER")

Dim sEnvKey, sEnvVal, aJBProducts
aJBProducts = Array("idea", "clion", "phpstorm", "goland", "pycharm", "webstorm", "webide", "rider", "datagrip", "rubymine", "appcode", "dataspell", "gateway", "jetbrains_client", "jetbrainsclient", "studio", "devecostudio")


For Each sPrd in aJBProducts
    sEnvKey = UCase(sPrd) & "_VM_OPTIONS"
    sEnvVal = oShell.ExpandEnvironmentStrings("%" & sEnvKey & "%")
    If sEnvVal <> ("%" & sEnvKey & "%") Then
        oEnv.Remove(sEnvKey)
    End If
Next

