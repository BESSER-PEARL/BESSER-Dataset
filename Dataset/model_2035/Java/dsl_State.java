





import java.util.List;
import java.util.ArrayList;

public class dsl_State  {

    private String name;





    private dsl_Statemachine dsl_statemachine;




    private List<dsl_State> dsl_states;




    private dsl_Statemachine dsl_statemachine;


    public dsl_State(
        String name    ) {
        this.name = name;
        this.dsl_states = new ArrayList<>();
    }

    public dsl_State(
        String name        ArrayList<dsl_State> dsl_states    ) {
        this.name = name;
        this.dsl_states = dsl_states;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public dsl_Statemachine getDsl_statemachine() {
        return dsl_statemachine;
    }

    public void setDsl_statemachine(dsl_Statemachine dsl_statemachine) {
        this.dsl_statemachine = dsl_statemachine;
    }
    public List<dsl_State> getDsl_states() {
        return dsl_states;
    }

    public void addDsl_state(Dsl_state dsl_state) {
        this.dsl_states.add(dsl_state);
    }
    public dsl_Statemachine getDsl_statemachine() {
        return dsl_statemachine;
    }

    public void setDsl_statemachine(dsl_Statemachine dsl_statemachine) {
        this.dsl_statemachine = dsl_statemachine;
    }

}