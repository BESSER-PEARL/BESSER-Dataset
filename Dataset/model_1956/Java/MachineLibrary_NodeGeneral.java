





import java.util.List;
import java.util.ArrayList;

public class MachineLibrary_NodeGeneral  {

    private String canCreateErrorTag;
    private String canCreateStateTag;





    private MachineLibrary_NodeConfig machinelibrary_nodeconfig;


    public MachineLibrary_NodeGeneral(
        String canCreateErrorTag,        String canCreateStateTag    ) {
        this.canCreateErrorTag = canCreateErrorTag;
        this.canCreateStateTag = canCreateStateTag;
    }


    public String getCancreateerrortag() {
        return canCreateErrorTag;
    }

    public void setCancreateerrortag(String canCreateErrorTag) {
        this.canCreateErrorTag = canCreateErrorTag;
    }
    public String getCancreatestatetag() {
        return canCreateStateTag;
    }

    public void setCancreatestatetag(String canCreateStateTag) {
        this.canCreateStateTag = canCreateStateTag;
    }

    public MachineLibrary_NodeConfig getMachinelibrary_nodeconfig() {
        return machinelibrary_nodeconfig;
    }

    public void setMachinelibrary_nodeconfig(MachineLibrary_NodeConfig machinelibrary_nodeconfig) {
        this.machinelibrary_nodeconfig = machinelibrary_nodeconfig;
    }

}