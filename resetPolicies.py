cmdSecurityPolicy=r'secedit /configure /cfg %windir%\inf\defltbase.inf /db defltbase.sdb /verbose'
cmdGroupPolicy=r'RD /S /Q "%WinDir%\System32\GroupPolicyUsers"'
cmdGroupPolicyUsers=r'RD /S /Q "%WinDir%\System32\GroupPolicy"'
cmdGPupdate=r'gpupdate /force'
import os;
import ctypes
class disable_file_system_redirection:
    _disable = ctypes.windll.kernel32.Wow64DisableWow64FsRedirection
    _revert = ctypes.windll.kernel32.Wow64RevertWow64FsRedirection
    def __enter__(self):
        self.old_value = ctypes.c_long()
        self.success = self._disable(ctypes.byref(self.old_value))
    def __exit__(self, type, value, traceback):
        if self.success:
            self._revert(self.old_value)
with disable_file_system_redirection():
    out=os.popen(cmdSecurityPolicy).read()
    out+=os.popen(cmdGroupPolicy).read()
    out+=os.popen(cmdGroupPolicyUsers).read()
    out+=os.popen(cmdGPupdate).read()
    print(out)
