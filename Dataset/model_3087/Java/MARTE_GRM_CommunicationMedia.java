





import java.util.List;
import java.util.ArrayList;

public class MARTE_GRM_CommunicationMedia extends ProcessingResource {

    private String transmMode;





    private NFP_Integer nfp_integer;


    public MARTE_GRM_CommunicationMedia(
        String transmMode    ) {
        super(
        );
        this.transmMode = transmMode;
    }


    public String getTransmmode() {
        return transmMode;
    }

    public void setTransmmode(String transmMode) {
        this.transmMode = transmMode;
    }

    public NFP_Integer getNfp_integer() {
        return nfp_integer;
    }

    public void setNfp_integer(NFP_Integer nfp_integer) {
        this.nfp_integer = nfp_integer;
    }

}