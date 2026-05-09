





import java.util.List;
import java.util.ArrayList;

public class gpfl_State  {

    private String name;





    private List<gpfl_Transition> gpfl_transitions;




    private gpfl_AutomataDef gpfl_automatadef;




    private gpfl_AutomataDef gpfl_automatadef;




    private gpfl_Transition gpfl_transition;


    public gpfl_State(
        String name    ) {
        this.name = name;
        this.gpfl_transitions = new ArrayList<>();
    }

    public gpfl_State(
        String name        ArrayList<gpfl_Transition> gpfl_transitions    ) {
        this.name = name;
        this.gpfl_transitions = gpfl_transitions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<gpfl_Transition> getGpfl_transitions() {
        return gpfl_transitions;
    }

    public void addGpfl_transition(Gpfl_transition gpfl_transition) {
        this.gpfl_transitions.add(gpfl_transition);
    }
    public gpfl_AutomataDef getGpfl_automatadef() {
        return gpfl_automatadef;
    }

    public void setGpfl_automatadef(gpfl_AutomataDef gpfl_automatadef) {
        this.gpfl_automatadef = gpfl_automatadef;
    }
    public gpfl_AutomataDef getGpfl_automatadef() {
        return gpfl_automatadef;
    }

    public void setGpfl_automatadef(gpfl_AutomataDef gpfl_automatadef) {
        this.gpfl_automatadef = gpfl_automatadef;
    }
    public gpfl_Transition getGpfl_transition() {
        return gpfl_transition;
    }

    public void setGpfl_transition(gpfl_Transition gpfl_transition) {
        this.gpfl_transition = gpfl_transition;
    }

}