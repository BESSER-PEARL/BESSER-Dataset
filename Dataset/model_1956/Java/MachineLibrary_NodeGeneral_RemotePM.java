





import java.util.List;
import java.util.ArrayList;

public class MachineLibrary_NodeGeneral_RemotePM  {

    private String system;
    private int timeServer;





    private MachineLibrary_NodeGeneralSpecial machinelibrary_nodegeneralspecial;


    public MachineLibrary_NodeGeneral_RemotePM(
        String system,        int timeServer    ) {
        this.system = system;
        this.timeServer = timeServer;
    }


    public String getSystem() {
        return system;
    }

    public void setSystem(String system) {
        this.system = system;
    }
    public int getTimeserver() {
        return timeServer;
    }

    public void setTimeserver(int timeServer) {
        this.timeServer = timeServer;
    }

    public MachineLibrary_NodeGeneralSpecial getMachinelibrary_nodegeneralspecial() {
        return machinelibrary_nodegeneralspecial;
    }

    public void setMachinelibrary_nodegeneralspecial(MachineLibrary_NodeGeneralSpecial machinelibrary_nodegeneralspecial) {
        this.machinelibrary_nodegeneralspecial = machinelibrary_nodegeneralspecial;
    }

}