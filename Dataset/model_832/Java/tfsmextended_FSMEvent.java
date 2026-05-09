





import java.util.List;
import java.util.ArrayList;

public class tfsmextended_FSMEvent extends NamedElement {

    private String isTriggered;





    private tfsmextended_TFSM tfsmextended_tfsm;


    public tfsmextended_FSMEvent(
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

    public tfsmextended_TFSM getTfsmextended_tfsm() {
        return tfsmextended_tfsm;
    }

    public void setTfsmextended_tfsm(tfsmextended_TFSM tfsmextended_tfsm) {
        this.tfsmextended_tfsm = tfsmextended_tfsm;
    }

}