





import java.util.List;
import java.util.ArrayList;

public class MachineLibrary_WS_Update_Host  {

    private int AllowUnit0;
    private int checkUnit;





    private MachineLibrary_UnitConfig_Host machinelibrary_unitconfig_host;


    public MachineLibrary_WS_Update_Host(
        int AllowUnit0,        int checkUnit    ) {
        this.AllowUnit0 = AllowUnit0;
        this.checkUnit = checkUnit;
    }


    public int getAllowunit0() {
        return AllowUnit0;
    }

    public void setAllowunit0(int AllowUnit0) {
        this.AllowUnit0 = AllowUnit0;
    }
    public int getCheckunit() {
        return checkUnit;
    }

    public void setCheckunit(int checkUnit) {
        this.checkUnit = checkUnit;
    }

    public MachineLibrary_UnitConfig_Host getMachinelibrary_unitconfig_host() {
        return machinelibrary_unitconfig_host;
    }

    public void setMachinelibrary_unitconfig_host(MachineLibrary_UnitConfig_Host machinelibrary_unitconfig_host) {
        this.machinelibrary_unitconfig_host = machinelibrary_unitconfig_host;
    }

}