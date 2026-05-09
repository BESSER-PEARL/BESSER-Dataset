





import java.util.List;
import java.util.ArrayList;

public class MachineLibrary_Units  {

    private int internalUniNo;
    private int unitNo;
    private String unitName;





    private MachineLibrary_NodeConfig machinelibrary_nodeconfig;


    public MachineLibrary_Units(
        int internalUniNo,        int unitNo,        String unitName    ) {
        this.internalUniNo = internalUniNo;
        this.unitNo = unitNo;
        this.unitName = unitName;
    }


    public int getInternalunino() {
        return internalUniNo;
    }

    public void setInternalunino(int internalUniNo) {
        this.internalUniNo = internalUniNo;
    }
    public int getUnitno() {
        return unitNo;
    }

    public void setUnitno(int unitNo) {
        this.unitNo = unitNo;
    }
    public String getUnitname() {
        return unitName;
    }

    public void setUnitname(String unitName) {
        this.unitName = unitName;
    }

    public MachineLibrary_NodeConfig getMachinelibrary_nodeconfig() {
        return machinelibrary_nodeconfig;
    }

    public void setMachinelibrary_nodeconfig(MachineLibrary_NodeConfig machinelibrary_nodeconfig) {
        this.machinelibrary_nodeconfig = machinelibrary_nodeconfig;
    }

}