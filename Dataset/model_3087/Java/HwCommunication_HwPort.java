





import java.util.List;
import java.util.ArrayList;

public class HwCommunication_HwPort  {






    private MARTE_HwDevice_HwPeripheral marte_hwdevice_hwperipheral;




    private MARTE_HwDevice_HwDevice marte_hwdevice_hwdevice;




    private MARTE_HwComputing_HwMCU marte_hwcomputing_hwmcu;


    public HwCommunication_HwPort(
    ) {
    }



    public MARTE_HwDevice_HwPeripheral getMarte_hwdevice_hwperipheral() {
        return marte_hwdevice_hwperipheral;
    }

    public void setMarte_hwdevice_hwperipheral(MARTE_HwDevice_HwPeripheral marte_hwdevice_hwperipheral) {
        this.marte_hwdevice_hwperipheral = marte_hwdevice_hwperipheral;
    }
    public MARTE_HwDevice_HwDevice getMarte_hwdevice_hwdevice() {
        return marte_hwdevice_hwdevice;
    }

    public void setMarte_hwdevice_hwdevice(MARTE_HwDevice_HwDevice marte_hwdevice_hwdevice) {
        this.marte_hwdevice_hwdevice = marte_hwdevice_hwdevice;
    }
    public MARTE_HwComputing_HwMCU getMarte_hwcomputing_hwmcu() {
        return marte_hwcomputing_hwmcu;
    }

    public void setMarte_hwcomputing_hwmcu(MARTE_HwComputing_HwMCU marte_hwcomputing_hwmcu) {
        this.marte_hwcomputing_hwmcu = marte_hwcomputing_hwmcu;
    }

}