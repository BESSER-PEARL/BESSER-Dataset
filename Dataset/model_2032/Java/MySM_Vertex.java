





import java.util.List;
import java.util.ArrayList;

public class MySM_Vertex  {






    private MySM_Transition mysm_transition;




    private MySM_Transition mysm_transition;




    private List<MySM_Transition> mysm_transitions;


    public MySM_Vertex(
    ) {
        this.mysm_transitions = new ArrayList<>();
    }

    public MySM_Vertex(
        ArrayList<MySM_Transition> mysm_transitions    ) {
        this.mysm_transitions = mysm_transitions;
    }


    public MySM_Transition getMysm_transition() {
        return mysm_transition;
    }

    public void setMysm_transition(MySM_Transition mysm_transition) {
        this.mysm_transition = mysm_transition;
    }
    public MySM_Transition getMysm_transition() {
        return mysm_transition;
    }

    public void setMysm_transition(MySM_Transition mysm_transition) {
        this.mysm_transition = mysm_transition;
    }
    public List<MySM_Transition> getMysm_transitions() {
        return mysm_transitions;
    }

    public void addMysm_transition(Mysm_transition mysm_transition) {
        this.mysm_transitions.add(mysm_transition);
    }

}