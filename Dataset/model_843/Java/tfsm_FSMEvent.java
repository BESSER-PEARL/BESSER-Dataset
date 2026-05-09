





import java.util.List;
import java.util.ArrayList;

public class tfsm_FSMEvent extends NamedElement {

    private String isTriggered;





    private tfsm_TFSM tfsm_tfsm;


    public tfsm_FSMEvent(
        String isTriggered    ) {
        super(
        );
        this.isTriggered = isTriggered;
    }


    public String getIstriggered() {
        return isTriggered;
    }

    public void setIstriggered(String isTriggered) {
        this.isTriggered = isTriggered;
    }

    public tfsm_TFSM getTfsm_tfsm() {
        return tfsm_tfsm;
    }

    public void setTfsm_tfsm(tfsm_TFSM tfsm_tfsm) {
        this.tfsm_tfsm = tfsm_tfsm;
    }

}