





import java.util.List;
import java.util.ArrayList;

public class MachineLibrary_Parameters  {

    private String parameterConfigYes;
    private String parameterConfigNo;





    private MachineLibrary_NodeConfig machinelibrary_nodeconfig;


    public MachineLibrary_Parameters(
        String parameterConfigYes,        String parameterConfigNo    ) {
        this.parameterConfigYes = parameterConfigYes;
        this.parameterConfigNo = parameterConfigNo;
    }


    public String getParameterconfigyes() {
        return parameterConfigYes;
    }

    public void setParameterconfigyes(String parameterConfigYes) {
        this.parameterConfigYes = parameterConfigYes;
    }
    public String getParameterconfigno() {
        return parameterConfigNo;
    }

    public void setParameterconfigno(String parameterConfigNo) {
        this.parameterConfigNo = parameterConfigNo;
    }

    public MachineLibrary_NodeConfig getMachinelibrary_nodeconfig() {
        return machinelibrary_nodeconfig;
    }

    public void setMachinelibrary_nodeconfig(MachineLibrary_NodeConfig machinelibrary_nodeconfig) {
        this.machinelibrary_nodeconfig = machinelibrary_nodeconfig;
    }

}