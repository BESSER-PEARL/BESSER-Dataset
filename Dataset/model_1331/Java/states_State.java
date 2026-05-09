





import java.util.List;
import java.util.ArrayList;

public class states_State  {






    private List<states_EObject> states_eobjects;




    private states_StateSystem states_statesystem;


    public states_State(
    ) {
        this.states_eobjects = new ArrayList<>();
    }

    public states_State(
        ArrayList<states_EObject> states_eobjects    ) {
        this.states_eobjects = states_eobjects;
    }


    public List<states_EObject> getStates_eobjects() {
        return states_eobjects;
    }

    public void addStates_eobject(States_eobject states_eobject) {
        this.states_eobjects.add(states_eobject);
    }
    public states_StateSystem getStates_statesystem() {
        return states_statesystem;
    }

    public void setStates_statesystem(states_StateSystem states_statesystem) {
        this.states_statesystem = states_statesystem;
    }

}