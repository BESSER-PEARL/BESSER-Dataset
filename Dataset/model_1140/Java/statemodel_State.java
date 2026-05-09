





import java.util.List;
import java.util.ArrayList;

public class statemodel_State extends Activity, Element {

    private String type;
    private String name;





    private statemodel_Transition statemodel_transition;




    private List<statemodel_Activity> statemodel_activitys;




    private statemodel_Statemachine statemodel_statemachine;


    public statemodel_State(
        String type,        String name    ) {
        super(
        );
        this.type = type;
        this.name = name;
        this.statemodel_activitys = new ArrayList<>();
    }

    public statemodel_State(
        String type,        String name        ArrayList<statemodel_Activity> statemodel_activitys    ) {
        this.type = type;
        this.name = name;
        this.statemodel_activitys = statemodel_activitys;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public statemodel_Transition getStatemodel_transition() {
        return statemodel_transition;
    }

    public void setStatemodel_transition(statemodel_Transition statemodel_transition) {
        this.statemodel_transition = statemodel_transition;
    }
    public List<statemodel_Activity> getStatemodel_activitys() {
        return statemodel_activitys;
    }

    public void addStatemodel_activity(Statemodel_activity statemodel_activity) {
        this.statemodel_activitys.add(statemodel_activity);
    }
    public statemodel_Statemachine getStatemodel_statemachine() {
        return statemodel_statemachine;
    }

    public void setStatemodel_statemachine(statemodel_Statemachine statemodel_statemachine) {
        this.statemodel_statemachine = statemodel_statemachine;
    }

}