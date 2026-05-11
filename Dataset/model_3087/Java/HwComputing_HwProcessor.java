





import java.util.List;
import java.util.ArrayList;

public class HwComputing_HwProcessor  {






    private MARTE_HwComputing_HwMCU marte_hwcomputing_hwmcu;




    private MARTE_HwStorageManager_HwDMA marte_hwstoragemanager_hwdma;


    public HwComputing_HwProcessor(
    ) {
    }



    public MARTE_HwComputing_HwMCU getMarte_hwcomputing_hwmcu() {
        return marte_hwcomputing_hwmcu;
    }

    public void setMarte_hwcomputing_hwmcu(MARTE_HwComputing_HwMCU marte_hwcomputing_hwmcu) {
        this.marte_hwcomputing_hwmcu = marte_hwcomputing_hwmcu;
    }
    public MARTE_HwStorageManager_HwDMA getMarte_hwstoragemanager_hwdma() {
        return marte_hwstoragemanager_hwdma;
    }

    public void setMarte_hwstoragemanager_hwdma(MARTE_HwStorageManager_HwDMA marte_hwstoragemanager_hwdma) {
        this.marte_hwstoragemanager_hwdma = marte_hwstoragemanager_hwdma;
    }

}