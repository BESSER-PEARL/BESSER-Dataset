





import java.util.List;
import java.util.ArrayList;

public class dsl_FSM  {

    private String name;





    private List<dsl_Transition> dsl_transitions;




    private dsl_InitialState dsl_initialstate;


    public dsl_FSM(
        String name    ) {
        this.name = name;
        this.dsl_transitions = new ArrayList<>();
    }

    public dsl_FSM(
        String name        ArrayList<dsl_Transition> dsl_transitions    ) {
        this.name = name;
        this.dsl_transitions = dsl_transitions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<dsl_Transition> getDsl_transitions() {
        return dsl_transitions;
    }

    public void addDsl_transition(Dsl_transition dsl_transition) {
        this.dsl_transitions.add(dsl_transition);
    }
    public dsl_InitialState getDsl_initialstate() {
        return dsl_initialstate;
    }

    public void setDsl_initialstate(dsl_InitialState dsl_initialstate) {
        this.dsl_initialstate = dsl_initialstate;
    }

}