





import java.util.List;
import java.util.ArrayList;

public class MachineLibrary_Position  {

    private int posExit;
    private String posRemark;
    private int posWarningOnDelete;
    private int posNo;
    private int posIndex;
    private String posName;





    private MachineLibrary_Positions machinelibrary_positions;


    public MachineLibrary_Position(
        int posExit,        String posRemark,        int posWarningOnDelete,        int posNo,        int posIndex,        String posName    ) {
        this.posExit = posExit;
        this.posRemark = posRemark;
        this.posWarningOnDelete = posWarningOnDelete;
        this.posNo = posNo;
        this.posIndex = posIndex;
        this.posName = posName;
    }


    public int getPosexit() {
        return posExit;
    }

    public void setPosexit(int posExit) {
        this.posExit = posExit;
    }
    public String getPosremark() {
        return posRemark;
    }

    public void setPosremark(String posRemark) {
        this.posRemark = posRemark;
    }
    public int getPoswarningondelete() {
        return posWarningOnDelete;
    }

    public void setPoswarningondelete(int posWarningOnDelete) {
        this.posWarningOnDelete = posWarningOnDelete;
    }
    public int getPosno() {
        return posNo;
    }

    public void setPosno(int posNo) {
        this.posNo = posNo;
    }
    public int getPosindex() {
        return posIndex;
    }

    public void setPosindex(int posIndex) {
        this.posIndex = posIndex;
    }
    public String getPosname() {
        return posName;
    }

    public void setPosname(String posName) {
        this.posName = posName;
    }

    public MachineLibrary_Positions getMachinelibrary_positions() {
        return machinelibrary_positions;
    }

    public void setMachinelibrary_positions(MachineLibrary_Positions machinelibrary_positions) {
        this.machinelibrary_positions = machinelibrary_positions;
    }

}