





import java.util.List;
import java.util.ArrayList;

public class shr5_PersonalAreaNetwork  {

    private int slaveMax;





    private shr5_MatrixDevice shr5_matrixdevice;




    private shr5_MatrixDevice shr5_matrixdevice;




    private List<shr5_MatrixDevice> shr5_matrixdevices;


    public shr5_PersonalAreaNetwork(
        int slaveMax    ) {
        this.slaveMax = slaveMax;
        this.shr5_matrixdevices = new ArrayList<>();
    }

    public shr5_PersonalAreaNetwork(
        int slaveMax        ArrayList<shr5_MatrixDevice> shr5_matrixdevices    ) {
        this.slaveMax = slaveMax;
        this.shr5_matrixdevices = shr5_matrixdevices;
    }

    public int getSlavemax() {
        return slaveMax;
    }

    public void setSlavemax(int slaveMax) {
        this.slaveMax = slaveMax;
    }

    public shr5_MatrixDevice getShr5_matrixdevice() {
        return shr5_matrixdevice;
    }

    public void setShr5_matrixdevice(shr5_MatrixDevice shr5_matrixdevice) {
        this.shr5_matrixdevice = shr5_matrixdevice;
    }
    public shr5_MatrixDevice getShr5_matrixdevice() {
        return shr5_matrixdevice;
    }

    public void setShr5_matrixdevice(shr5_MatrixDevice shr5_matrixdevice) {
        this.shr5_matrixdevice = shr5_matrixdevice;
    }
    public List<shr5_MatrixDevice> getShr5_matrixdevices() {
        return shr5_matrixdevices;
    }

    public void addShr5_matrixdevice(Shr5_matrixdevice shr5_matrixdevice) {
        this.shr5_matrixdevices.add(shr5_matrixdevice);
    }

}