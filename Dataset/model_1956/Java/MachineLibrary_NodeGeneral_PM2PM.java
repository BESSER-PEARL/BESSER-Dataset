





import java.util.List;
import java.util.ArrayList;

public class MachineLibrary_NodeGeneral_PM2PM  {

    private int timeServer;
    private int type;





    private MachineLibrary_NodeGeneralSpecial machinelibrary_nodegeneralspecial;


    public MachineLibrary_NodeGeneral_PM2PM(
        int timeServer,        int type    ) {
        this.timeServer = timeServer;
        this.type = type;
    }


    public int getTimeserver() {
        return timeServer;
    }

    public void setTimeserver(int timeServer) {
        this.timeServer = timeServer;
    }
    public int getType() {
        return type;
    }

    public void setType(int type) {
        this.type = type;
    }

    public MachineLibrary_NodeGeneralSpecial getMachinelibrary_nodegeneralspecial() {
        return machinelibrary_nodegeneralspecial;
    }

    public void setMachinelibrary_nodegeneralspecial(MachineLibrary_NodeGeneralSpecial machinelibrary_nodegeneralspecial) {
        this.machinelibrary_nodegeneralspecial = machinelibrary_nodegeneralspecial;
    }

}