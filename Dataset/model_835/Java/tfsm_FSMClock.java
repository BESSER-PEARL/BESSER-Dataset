





import java.util.List;
import java.util.ArrayList;

public class tfsm_FSMClock extends NamedElement {

    private boolean numberOfTicks;





    private tfsm_TFSM tfsm_tfsm;


    public tfsm_FSMClock(
        boolean numberOfTicks    ) {
        super(
        );
        this.numberOfTicks = numberOfTicks;
    }


    public boolean getNumberofticks() {
        return numberOfTicks;
    }

    public void setNumberofticks(boolean numberOfTicks) {
        this.numberOfTicks = numberOfTicks;
    }

    public tfsm_TFSM getTfsm_tfsm() {
        return tfsm_tfsm;
    }

    public void setTfsm_tfsm(tfsm_TFSM tfsm_tfsm) {
        this.tfsm_tfsm = tfsm_tfsm;
    }

}