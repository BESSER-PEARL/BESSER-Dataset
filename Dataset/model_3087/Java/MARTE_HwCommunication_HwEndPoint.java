





import java.util.List;
import java.util.ArrayList;

public class MARTE_HwCommunication_HwEndPoint extends HwCommunication_HwCommunicationResource, GRM_CommunicationEndPoint {






    private List<HwCommunication_HwMedia> hwcommunication_hwmedias;


    public MARTE_HwCommunication_HwEndPoint(
    ) {
        super(
        );
        this.hwcommunication_hwmedias = new ArrayList<>();
    }

    public MARTE_HwCommunication_HwEndPoint(
        ArrayList<HwCommunication_HwMedia> hwcommunication_hwmedias    ) {
        this.hwcommunication_hwmedias = hwcommunication_hwmedias;
    }


    public List<HwCommunication_HwMedia> getHwcommunication_hwmedias() {
        return hwcommunication_hwmedias;
    }

    public void addHwcommunication_hwmedia(Hwcommunication_hwmedia hwcommunication_hwmedia) {
        this.hwcommunication_hwmedias.add(hwcommunication_hwmedia);
    }

}