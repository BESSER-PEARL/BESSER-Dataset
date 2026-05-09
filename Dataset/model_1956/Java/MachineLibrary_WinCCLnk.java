





import java.util.List;
import java.util.ArrayList;

public class MachineLibrary_WinCCLnk  {

    private int updateCycle;
    private int canCreateTags;
    private int canModifyTag;
    private String connectionName;
    private String updateCycle_Help;





    private MachineLibrary_LinkConfig machinelibrary_linkconfig;


    public MachineLibrary_WinCCLnk(
        int updateCycle,        int canCreateTags,        int canModifyTag,        String connectionName,        String updateCycle_Help    ) {
        this.updateCycle = updateCycle;
        this.canCreateTags = canCreateTags;
        this.canModifyTag = canModifyTag;
        this.connectionName = connectionName;
        this.updateCycle_Help = updateCycle_Help;
    }


    public int getUpdatecycle() {
        return updateCycle;
    }

    public void setUpdatecycle(int updateCycle) {
        this.updateCycle = updateCycle;
    }
    public int getCancreatetags() {
        return canCreateTags;
    }

    public void setCancreatetags(int canCreateTags) {
        this.canCreateTags = canCreateTags;
    }
    public int getCanmodifytag() {
        return canModifyTag;
    }

    public void setCanmodifytag(int canModifyTag) {
        this.canModifyTag = canModifyTag;
    }
    public String getConnectionname() {
        return connectionName;
    }

    public void setConnectionname(String connectionName) {
        this.connectionName = connectionName;
    }
    public String getUpdatecycle_help() {
        return updateCycle_Help;
    }

    public void setUpdatecycle_help(String updateCycle_Help) {
        this.updateCycle_Help = updateCycle_Help;
    }

    public MachineLibrary_LinkConfig getMachinelibrary_linkconfig() {
        return machinelibrary_linkconfig;
    }

    public void setMachinelibrary_linkconfig(MachineLibrary_LinkConfig machinelibrary_linkconfig) {
        this.machinelibrary_linkconfig = machinelibrary_linkconfig;
    }

}