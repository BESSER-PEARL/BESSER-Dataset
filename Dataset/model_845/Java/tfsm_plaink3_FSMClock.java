





import java.util.List;
import java.util.ArrayList;

public class tfsm_plaink3_FSMClock extends NamedElement {

    private String numberOfTicks;





    private tfsm_plaink3_TFSM tfsm_plaink3_tfsm;


    public tfsm_plaink3_FSMClock(
        String numberOfTicks    ) {
        super(
        );
        this.numberOfTicks = numberOfTicks;
    }


    public String getNumberofticks() {
        return numberOfTicks;
    }

    public void setNumberofticks(String numberOfTicks) {
        this.numberOfTicks = numberOfTicks;
    }

    public tfsm_plaink3_TFSM getTfsm_plaink3_tfsm() {
        return tfsm_plaink3_tfsm;
    }

    public void setTfsm_plaink3_tfsm(tfsm_plaink3_TFSM tfsm_plaink3_tfsm) {
        this.tfsm_plaink3_tfsm = tfsm_plaink3_tfsm;
    }

}