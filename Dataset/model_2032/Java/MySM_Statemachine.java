





import java.util.List;
import java.util.ArrayList;

public class MySM_Statemachine extends Region {






    private List<MySM_Action> mysm_actions;




    private List<MySM_Transition> mysm_transitions;


    public MySM_Statemachine(
    ) {
        super(
        );
        this.mysm_actions = new ArrayList<>();
        this.mysm_transitions = new ArrayList<>();
    }

    public MySM_Statemachine(
        ArrayList<MySM_Action> mysm_actions,        ArrayList<MySM_Transition> mysm_transitions    ) {
        this.mysm_actions = mysm_actions;
        this.mysm_transitions = mysm_transitions;
    }


    public List<MySM_Action> getMysm_actions() {
        return mysm_actions;
    }

    public void addMysm_action(Mysm_action mysm_action) {
        this.mysm_actions.add(mysm_action);
    }
    public List<MySM_Transition> getMysm_transitions() {
        return mysm_transitions;
    }

    public void addMysm_transition(Mysm_transition mysm_transition) {
        this.mysm_transitions.add(mysm_transition);
    }

}