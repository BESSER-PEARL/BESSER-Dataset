





import java.util.List;
import java.util.ArrayList;

public class tfsm_FSMClock extends NamedElement {

    private String numberOfTicks;





    private tfsm_TimedSystem tfsm_timedsystem;




    private tfsm_TFSM tfsm_tfsm;


    public tfsm_FSMClock(
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