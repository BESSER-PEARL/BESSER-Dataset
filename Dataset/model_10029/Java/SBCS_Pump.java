





import java.util.List;
import java.util.ArrayList;

public class SBCS_Pump  {

    private String mode;





    private SBCS_PumpControler sbcs_pumpcontroler;


    public SBCS_Pump(
        String mode    ) {
        this.mode = mode;
    }


    public String getMode() {
        return mode;
    }

    public void setMode(String mode) {
        this.mode = mode;
    }

    public SBCS_PumpControler getSbcs_pumpcontroler() {
        return sbcs_pumpcontroler;
    }

    public void setSbcs_pumpcontroler(SBCS_PumpControler sbcs_pumpcontroler) {
        this.sbcs_pumpcontroler = sbcs_pumpcontroler;
    }

}