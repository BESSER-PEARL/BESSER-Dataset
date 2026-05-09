





import java.util.List;
import java.util.ArrayList;

public class tfsmextended_FSMEvent extends NamedElement {

    private boolean isTriggered;





    private tfsmextended_TFSM tfsmextended_tfsm;


    public tfsmextended_FSMEvent(
        boolean isTriggered    ) {
        super(
        );
        this.isTriggered = isTriggered;
    }


    public boolean getIstriggered() {
        return isTriggered;
    }

    public void setIstriggered(boolean isTriggered) {
        this.isTriggered = isTriggered;
    }

    public tfsmextended_TFSM getTfsmextended_tfsm() {
        return tfsmextended_tfsm;
    }

    public void setTfsmextended_tfsm(tfsmextended_TFSM tfsmextended_tfsm) {
        this.tfsmextended_tfsm = tfsmextended_tfsm;
    }

}