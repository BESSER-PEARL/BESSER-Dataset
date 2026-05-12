





import java.util.List;
import java.util.ArrayList;

public class smachDSL_ActionState  {

    private String name;





    private smachDSL_ActionClient smachdsl_actionclient;




    private smachDSL_Transition smachdsl_transition;




    private List<smachDSL_Transition> smachdsl_transitions;




    private smachDSL_StateMachine smachdsl_statemachine;


    public smachDSL_ActionState(
        String name    ) {
        this.name = name;
        this.smachdsl_transitions = new ArrayList<>();
    }

    public smachDSL_ActionState(
        String name        ArrayList<smachDSL_Transition> smachdsl_transitions    ) {
        this.name = name;
        this.smachdsl_transitions = smachdsl_transitions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public smachDSL_ActionClient getSmachdsl_actionclient() {
        return smachdsl_actionclient;
    }

    public void setSmachdsl_actionclient(smachDSL_ActionClient smachdsl_actionclient) {
        this.smachdsl_actionclient = smachdsl_actionclient;
    }
    public smachDSL_Transition getSmachdsl_transition() {
        return smachdsl_transition;
    }

    public void setSmachdsl_transition(smachDSL_Transition smachdsl_transition) {
        this.smachdsl_transition = smachdsl_transition;
    }
    public List<smachDSL_Transition> getSmachdsl_transitions() {
        return smachdsl_transitions;
    }

    public void addSmachdsl_transition(Smachdsl_transition smachdsl_transition) {
        this.smachdsl_transitions.add(smachdsl_transition);
    }
    public smachDSL_StateMachine getSmachdsl_statemachine() {
        return smachdsl_statemachine;
    }

    public void setSmachdsl_statemachine(smachDSL_StateMachine smachdsl_statemachine) {
        this.smachdsl_statemachine = smachdsl_statemachine;
    }

}