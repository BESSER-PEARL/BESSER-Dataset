





import java.util.List;
import java.util.ArrayList;

public class MARTE_HwCommunication_HwMedia extends HwCommunication_HwCommunicationResource, GRM_CommunicationMedia {






    private List<HwCommunication_HwArbiter> hwcommunication_hwarbiters;




    private NFP_DataTxRate nfp_datatxrate;


    public MARTE_HwCommunication_HwMedia(
    ) {
        super(
        );
        this.hwcommunication_hwarbiters = new ArrayList<>();
    }

    public MARTE_HwCommunication_HwMedia(
        ArrayList<HwCommunication_HwArbiter> hwcommunication_hwarbiters    ) {
        this.hwcommunication_hwarbiters = hwcommunication_hwarbiters;
    }


    public List<HwCommunication_HwArbiter> getHwcommunication_hwarbiters() {
        return hwcommunication_hwarbiters;
    }

    public void addHwcommunication_hwarbiter(Hwcommunication_hwarbiter hwcommunication_hwarbiter) {
        this.hwcommunication_hwarbiters.add(hwcommunication_hwarbiter);
    }
    public NFP_DataTxRate getNfp_datatxrate() {
        return nfp_datatxrate;
    }

    public void setNfp_datatxrate(NFP_DataTxRate nfp_datatxrate) {
        this.nfp_datatxrate = nfp_datatxrate;
    }

}