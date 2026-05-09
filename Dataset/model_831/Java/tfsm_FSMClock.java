





import java.util.List;
import java.util.ArrayList;

public class tfsm_FSMClock extends NamedElement {

    private int numberOfTicks;





    private tfsm_TimedSystem tfsm_timedsystem;




    private tfsm_TFSM tfsm_tfsm;


    public tfsm_FSMClock(
        int numberOfTicks    ) {
        super(
        );
        this.numberOfTicks = numberOfTicks;
    }


    public int getNumberofticks() {
        return numberOfTicks;
    }

    public void setNumberofticks(int numberOfTicks) {
        this.numberOfTicks = numberOfTicks;
    }

    public tfsm_TimedSystem getTfsm_timedsystem() {
        return tfsm_timedsystem;
    }

    public void setTfsm_timedsystem(tfsm_TimedSystem tfsm_timedsystem) {
        this.tfsm_timedsystem = tfsm_timedsystem;
    }
    public tfsm_TFSM getTfsm_tfsm() {
        return tfsm_tfsm;
    }

    public void setTfsm_tfsm(tfsm_TFSM tfsm_tfsm) {
        this.tfsm_tfsm = tfsm_tfsm;
    }

}