





import java.util.List;
import java.util.ArrayList;

public class MARTE_Time_Clock  {

    private String standard;





    private NFPs_Unit nfps_unit;


    public MARTE_Time_Clock(
        String standard    ) {
        this.standard = standard;
    }


    public String getStandard() {
        return standard;
    }

    public void setStandard(String standard) {
        this.standard = standard;
    }

    public NFPs_Unit getNfps_unit() {
        return nfps_unit;
    }

    public void setNfps_unit(NFPs_Unit nfps_unit) {
        this.nfps_unit = nfps_unit;
    }

}