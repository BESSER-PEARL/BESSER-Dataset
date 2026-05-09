





import java.util.List;
import java.util.ArrayList;

public class tfsm_Transition extends NamedElement {

    private String action;





    private tfsm_TFSM tfsm_tfsm;


    public tfsm_Transition(
        String action    ) {
        super(
        );
        this.action = action;
    }


    public String getAction() {
        return action;
    }

    public void setAction(String action) {
        this.action = action;
    }

    public tfsm_TFSM getTfsm_tfsm() {
        return tfsm_tfsm;
    }

    public void setTfsm_tfsm(tfsm_TFSM tfsm_tfsm) {
        this.tfsm_tfsm = tfsm_tfsm;
    }

}