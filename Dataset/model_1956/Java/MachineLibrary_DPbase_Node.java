





import java.util.List;
import java.util.ArrayList;

public class MachineLibrary_DPbase_Node  {

    private int isXPS;
    private int nodeNo;





    private MachineLibrary_DPbase_Link machinelibrary_dpbase_link;


    public MachineLibrary_DPbase_Node(
        int isXPS,        int nodeNo    ) {
        this.isXPS = isXPS;
        this.nodeNo = nodeNo;
    }


    public int getIsxps() {
        return isXPS;
    }

    public void setIsxps(int isXPS) {
        this.isXPS = isXPS;
    }
    public int getNodeno() {
        return nodeNo;
    }

    public void setNodeno(int nodeNo) {
        this.nodeNo = nodeNo;
    }

    public MachineLibrary_DPbase_Link getMachinelibrary_dpbase_link() {
        return machinelibrary_dpbase_link;
    }

    public void setMachinelibrary_dpbase_link(MachineLibrary_DPbase_Link machinelibrary_dpbase_link) {
        this.machinelibrary_dpbase_link = machinelibrary_dpbase_link;
    }

}