





import java.util.List;
import java.util.ArrayList;

public class umlTrace_Values_ActionActivation_firing_Value  {

    private boolean firing;





    private List<Values_umlTrace_State> values_umltrace_states;


    public umlTrace_Values_ActionActivation_firing_Value(
        boolean firing    ) {
        this.firing = firing;
        this.values_umltrace_states = new ArrayList<>();
    }

    public umlTrace_Values_ActionActivation_firing_Value(
        boolean firing        ArrayList<Values_umlTrace_State> values_umltrace_states    ) {
        this.firing = firing;
        this.values_umltrace_states = values_umltrace_states;
    }

    public boolean getFiring() {
        return firing;
    }

    public void setFiring(boolean firing) {
        this.firing = firing;
    }

    public List<Values_umlTrace_State> getValues_umltrace_states() {
        return values_umltrace_states;
    }

    public void addValues_umltrace_state(Values_umltrace_state values_umltrace_state) {
        this.values_umltrace_states.add(values_umltrace_state);
    }

}