





import java.util.List;
import java.util.ArrayList;

public class MachineLibrary_NodeConfig  {

    private int nodeNo;
    private String simFileName;
    private String nodeName;





    private MachineLibrary_LabMachine machinelibrary_labmachine;


    public MachineLibrary_NodeConfig(
        int nodeNo,        String simFileName,        String nodeName    ) {
        this.nodeNo = nodeNo;
        this.simFileName = simFileName;
        this.nodeName = nodeName;
    }


    public int getNodeno() {
        return nodeNo;
    }

    public void setNodeno(int nodeNo) {
        this.nodeNo = nodeNo;
    }
    public String getSimfilename() {
        return simFileName;
    }

    public void setSimfilename(String simFileName) {
        this.simFileName = simFileName;
    }
    public String getNodename() {
        return nodeName;
    }

    public void setNodename(String nodeName) {
        this.nodeName = nodeName;
    }

    public MachineLibrary_LabMachine getMachinelibrary_labmachine() {
        return machinelibrary_labmachine;
    }

    public void setMachinelibrary_labmachine(MachineLibrary_LabMachine machinelibrary_labmachine) {
        this.machinelibrary_labmachine = machinelibrary_labmachine;
    }

}