





import java.util.List;
import java.util.ArrayList;

public class petrinetv3Trace_petrinetv3_TracedTransition  {






    private List<petrinetv3_TracedPlace> petrinetv3_tracedplaces;




    private petrinetv3_petrinetv3Trace_Net petrinetv3_petrinetv3trace_net;




    private petrinetv3_petrinetv3Trace_Transition petrinetv3_petrinetv3trace_transition;




    private List<petrinetv3_TracedPlace> petrinetv3_tracedplaces;




    private List<Transition_clock_Value> transition_clock_values;


    public petrinetv3Trace_petrinetv3_TracedTransition(
    ) {
        this.petrinetv3_tracedplaces = new ArrayList<>();
        this.petrinetv3_tracedplaces = new ArrayList<>();
        this.transition_clock_values = new ArrayList<>();
    }

    public petrinetv3Trace_petrinetv3_TracedTransition(
        ArrayList<petrinetv3_TracedPlace> petrinetv3_tracedplaces,        ArrayList<petrinetv3_TracedPlace> petrinetv3_tracedplaces,        ArrayList<Transition_clock_Value> transition_clock_values    ) {
        this.petrinetv3_tracedplaces = petrinetv3_tracedplaces;
        this.petrinetv3_tracedplaces = petrinetv3_tracedplaces;
        this.transition_clock_values = transition_clock_values;
    }


    public List<petrinetv3_TracedPlace> getPetrinetv3_tracedplaces() {
        return petrinetv3_tracedplaces;
    }

    public void addPetrinetv3_tracedplace(Petrinetv3_tracedplace petrinetv3_tracedplace) {
        this.petrinetv3_tracedplaces.add(petrinetv3_tracedplace);
    }
    public petrinetv3_petrinetv3Trace_Net getPetrinetv3_petrinetv3trace_net() {
        return petrinetv3_petrinetv3trace_net;
    }

    public void setPetrinetv3_petrinetv3trace_net(petrinetv3_petrinetv3Trace_Net petrinetv3_petrinetv3trace_net) {
        this.petrinetv3_petrinetv3trace_net = petrinetv3_petrinetv3trace_net;
    }
    public petrinetv3_petrinetv3Trace_Transition getPetrinetv3_petrinetv3trace_transition() {
        return petrinetv3_petrinetv3trace_transition;
    }

    public void setPetrinetv3_petrinetv3trace_transition(petrinetv3_petrinetv3Trace_Transition petrinetv3_petrinetv3trace_transition) {
        this.petrinetv3_petrinetv3trace_transition = petrinetv3_petrinetv3trace_transition;
    }
    public List<petrinetv3_TracedPlace> getPetrinetv3_tracedplaces() {
        return petrinetv3_tracedplaces;
    }

    public void addPetrinetv3_tracedplace(Petrinetv3_tracedplace petrinetv3_tracedplace) {
        this.petrinetv3_tracedplaces.add(petrinetv3_tracedplace);
    }
    public List<Transition_clock_Value> getTransition_clock_values() {
        return transition_clock_values;
    }

    public void addTransition_clock_value(Transition_clock_value transition_clock_value) {
        this.transition_clock_values.add(transition_clock_value);
    }

}