





import java.util.List;
import java.util.ArrayList;

public class MARTE_HwStorageManager_HwDMA extends HwCommunication_HwArbiter, HwStorageManager_HwStorageManager {






    private NFP_Natural nfp_natural;




    private NFP_DataSize nfp_datasize;


    public MARTE_HwStorageManager_HwDMA(
    ) {
        super(
        );
    }



    public NFP_Natural getNfp_natural() {
        return nfp_natural;
    }

    public void setNfp_natural(NFP_Natural nfp_natural) {
        this.nfp_natural = nfp_natural;
    }
    public NFP_DataSize getNfp_datasize() {
        return nfp_datasize;
    }

    public void setNfp_datasize(NFP_DataSize nfp_datasize) {
        this.nfp_datasize = nfp_datasize;
    }

}