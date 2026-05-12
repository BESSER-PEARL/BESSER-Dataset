





import java.util.List;
import java.util.ArrayList;

public class states_Event  {

    private String qualifiedName;





    private states_Transition states_transition;


    public states_Event(
        String qualifiedName    ) {
        this.qualifiedName = qualifiedName;
    }


    public String getQualifiedname() {
        return qualifiedName;
    }

    public void setQualifiedname(String qualifiedName) {
        this.qualifiedName = qualifiedName;
    }

    public states_Transition getStates_transition() {
        return states_transition;
    }

    public void setStates_transition(states_Transition states_transition) {
        this.states_transition = states_transition;
    }

}