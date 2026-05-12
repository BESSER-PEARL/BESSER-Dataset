





import java.util.List;
import java.util.ArrayList;

public class state_State extends NamedElement, Vertex {

    private boolean isSimple;
    private boolean isComposite;





    private List<state_Trigger> state_triggers;


    public state_State(
        boolean isSimple,        boolean isComposite    ) {
        super(
        );
        this.isSimple = isSimple;
        this.isComposite = isComposite;
        this.state_triggers = new ArrayList<>();
    }

    public state_State(
        boolean isSimple,        boolean isComposite        ArrayList<state_Trigger> state_triggers    ) {
        this.isSimple = isSimple;
        this.isComposite = isComposite;
        this.state_triggers = state_triggers;
    }

    public boolean getIssimple() {
        return isSimple;
    }

    public void setIssimple(boolean isSimple) {
        this.isSimple = isSimple;
    }
    public boolean getIscomposite() {
        return isComposite;
    }

    public void setIscomposite(boolean isComposite) {
        this.isComposite = isComposite;
    }

    public List<state_Trigger> getState_triggers() {
        return state_triggers;
    }

    public void addState_trigger(State_trigger state_trigger) {
        this.state_triggers.add(state_trigger);
    }

}