





import java.util.List;
import java.util.ArrayList;

public class MARTE_Library_BasicNFP_Types_OpenPattern  {

    private String arrivalProcess;





    private NFP_Duration nfp_duration;


    public MARTE_Library_BasicNFP_Types_OpenPattern(
        String arrivalProcess    ) {
        this.arrivalProcess = arrivalProcess;
    }


    public String getArrivalprocess() {
        return arrivalProcess;
    }

    public void setArrivalprocess(String arrivalProcess) {
        this.arrivalProcess = arrivalProcess;
    }

    public NFP_Duration getNfp_duration() {
        return nfp_duration;
    }

    public void setNfp_duration(NFP_Duration nfp_duration) {
        this.nfp_duration = nfp_duration;
    }

}