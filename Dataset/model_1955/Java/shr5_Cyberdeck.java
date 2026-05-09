





import java.util.List;
import java.util.ArrayList;

public class shr5_Cyberdeck extends Capacity, AbstractMatrixDevice, ActiveMatixDevice, MatrixDevice {

    private int attribute3;
    private String modManager;
    private int programSlots;
    private int attribute2;
    private int attribute1;
    private int attribute4;



    public shr5_Cyberdeck(
        int attribute3,        String modManager,        int programSlots,        int attribute2,        int attribute1,        int attribute4    ) {
        super(
        );
        this.attribute3 = attribute3;
        this.modManager = modManager;
        this.programSlots = programSlots;
        this.attribute2 = attribute2;
        this.attribute1 = attribute1;
        this.attribute4 = attribute4;
    }


    public int getAttribute3() {
        return attribute3;
    }

    public void setAttribute3(int attribute3) {
        this.attribute3 = attribute3;
    }
    public String getModmanager() {
        return modManager;
    }

    public void setModmanager(String modManager) {
        this.modManager = modManager;
    }
    public int getProgramslots() {
        return programSlots;
    }

    public void setProgramslots(int programSlots) {
        this.programSlots = programSlots;
    }
    public int getAttribute2() {
        return attribute2;
    }

    public void setAttribute2(int attribute2) {
        this.attribute2 = attribute2;
    }
    public int getAttribute1() {
        return attribute1;
    }

    public void setAttribute1(int attribute1) {
        this.attribute1 = attribute1;
    }
    public int getAttribute4() {
        return attribute4;
    }

    public void setAttribute4(int attribute4) {
        this.attribute4 = attribute4;
    }


}