





import java.util.List;
import java.util.ArrayList;

public class state_Transition extends NamedElement {

    private String kind;





    private state_Trigger state_trigger;




    private state_Region state_region;


    public state_Transition(
        String kind    ) {
        super(
        );
        this.kind = kind;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public state_Trigger getState_trigger() {
        return state_trigger;
    }

    public void setState_trigger(state_Trigger state_trigger) {
        this.state_trigger = state_trigger;
    }
    public state_Region getState_region() {
        return state_region;
    }

    public void setState_region(state_Region state_region) {
        this.state_region = state_region;
    }

}