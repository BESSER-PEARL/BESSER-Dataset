





import java.util.List;
import java.util.ArrayList;

public class MMInterModel_StateMachine extends Element {

    private String superState;
    private String component;
    private String type;





    private List<MMInterModel_State> mmintermodel_states;




    private MMInterModel_State mmintermodel_state;




    private List<MMInterModel_Transition> mmintermodel_transitions;




    private MMInterModel_State mmintermodel_state;


    public MMInterModel_StateMachine(
        String superState,        String component,        String type    ) {
        super(
        );
        this.superState = superState;
        this.component = component;
        this.type = type;
        this.mmintermodel_states = new ArrayList<>();
        this.mmintermodel_transitions = new ArrayList<>();
    }

    public MMInterModel_StateMachine(
        String superState,        String component,        String type        ArrayList<MMInterModel_State> mmintermodel_states,        ArrayList<MMInterModel_Transition> mmintermodel_transitions    ) {
        this.superState = superState;
        this.component = component;
        this.type = type;
        this.mmintermodel_states = mmintermodel_states;
        this.mmintermodel_transitions = mmintermodel_transitions;
    }

    public String getSuperstate() {
        return superState;
    }

    public void setSuperstate(String superState) {
        this.superState = superState;
    }
    public String getComponent() {
        return component;
    }

    public void setComponent(String component) {
        this.component = component;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public List<MMInterModel_State> getMmintermodel_states() {
        return mmintermodel_states;
    }

    public void addMmintermodel_state(Mmintermodel_state mmintermodel_state) {
        this.mmintermodel_states.add(mmintermodel_state);
    }
    public MMInterModel_State getMmintermodel_state() {
        return mmintermodel_state;
    }

    public void setMmintermodel_state(MMInterModel_State mmintermodel_state) {
        this.mmintermodel_state = mmintermodel_state;
    }
    public List<MMInterModel_Transition> getMmintermodel_transitions() {
        return mmintermodel_transitions;
    }

    public void addMmintermodel_transition(Mmintermodel_transition mmintermodel_transition) {
        this.mmintermodel_transitions.add(mmintermodel_transition);
    }
    public MMInterModel_State getMmintermodel_state() {
        return mmintermodel_state;
    }

    public void setMmintermodel_state(MMInterModel_State mmintermodel_state) {
        this.mmintermodel_state = mmintermodel_state;
    }

}