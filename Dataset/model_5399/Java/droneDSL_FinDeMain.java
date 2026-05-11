





import java.util.List;
import java.util.ArrayList;

public class droneDSL_FinDeMain  {

    private String accolade;





    private droneDSL_Main dronedsl_main;


    public droneDSL_FinDeMain(
        String accolade    ) {
        this.accolade = accolade;
    }


    public String getAccolade() {
        return accolade;
    }

    public void setAccolade(String accolade) {
        this.accolade = accolade;
    }

    public droneDSL_Main getDronedsl_main() {
        return dronedsl_main;
    }

    public void setDronedsl_main(droneDSL_Main dronedsl_main) {
        this.dronedsl_main = dronedsl_main;
    }

}