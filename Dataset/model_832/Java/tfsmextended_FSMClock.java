





import java.util.List;
import java.util.ArrayList;

public class tfsmextended_FSMClock extends NamedElement {

    private String numberOfTicks;





    private tfsmextended_TFSM tfsmextended_tfsm;


    public tfsmextended_FSMClock(
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

    public tfsmextended_TFSM getTfsmextended_tfsm() {
        return tfsmextended_tfsm;
    }

    public void setTfsmextended_tfsm(tfsmextended_TFSM tfsmextended_tfsm) {
        this.tfsmextended_tfsm = tfsmextended_tfsm;
    }

}