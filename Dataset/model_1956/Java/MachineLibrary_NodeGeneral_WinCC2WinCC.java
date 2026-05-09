





import java.util.List;
import java.util.ArrayList;

public class MachineLibrary_NodeGeneral_WinCC2WinCC  {

    private String prefix;





    private MachineLibrary_NodeGeneralSpecial machinelibrary_nodegeneralspecial;


    public MachineLibrary_NodeGeneral_WinCC2WinCC(
        String prefix    ) {
        this.prefix = prefix;
    }


    public String getPrefix() {
        return prefix;
    }

    public void setPrefix(String prefix) {
        this.prefix = prefix;
    }

    public MachineLibrary_NodeGeneralSpecial getMachinelibrary_nodegeneralspecial() {
        return machinelibrary_nodegeneralspecial;
    }

    public void setMachinelibrary_nodegeneralspecial(MachineLibrary_NodeGeneralSpecial machinelibrary_nodegeneralspecial) {
        this.machinelibrary_nodegeneralspecial = machinelibrary_nodegeneralspecial;
    }

}