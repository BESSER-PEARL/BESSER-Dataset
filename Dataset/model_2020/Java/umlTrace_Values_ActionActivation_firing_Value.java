





import java.util.List;
import java.util.ArrayList;

public class umlTrace_Values_ActionActivation_firing_Value  {

    private String firing;





    private List<State> states;


    public umlTrace_Values_ActionActivation_firing_Value(
        String firing    ) {
        this.firing = firing;
        this.states = new ArrayList<>();
    }

    public umlTrace_Values_ActionActivation_firing_Value(
        String firing        ArrayList<State> states    ) {
        this.firing = firing;
        this.states = states;
    }

    public String getFiring() {
        return firing;
    }

    public void setFiring(String firing) {
        this.firing = firing;
    }

    public List<State> getStates() {
        return states;
    }

    public void addState(State state) {
        this.states.add(state);
    }

}