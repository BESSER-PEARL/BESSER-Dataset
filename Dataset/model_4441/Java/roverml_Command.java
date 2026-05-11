





import java.util.List;
import java.util.ArrayList;

public class roverml_Command  {






    private List<roverml_Transition> roverml_transitions;




    private roverml_Block roverml_block;




    private List<roverml_Component> roverml_components;




    private roverml_Transition roverml_transition;




    private List<roverml_Transition> roverml_transitions;




    private roverml_Transition roverml_transition;


    public roverml_Command(
    ) {
        this.roverml_transitions = new ArrayList<>();
        this.roverml_components = new ArrayList<>();
        this.roverml_transitions = new ArrayList<>();
    }

    public roverml_Command(
        ArrayList<roverml_Transition> roverml_transitions,        ArrayList<roverml_Component> roverml_components,        ArrayList<roverml_Transition> roverml_transitions    ) {
        this.roverml_transitions = roverml_transitions;
        this.roverml_components = roverml_components;
        this.roverml_transitions = roverml_transitions;
    }


    public List<roverml_Transition> getRoverml_transitions() {
        return roverml_transitions;
    }

    public void addRoverml_transition(Roverml_transition roverml_transition) {
        this.roverml_transitions.add(roverml_transition);
    }
    public roverml_Block getRoverml_block() {
        return roverml_block;
    }

    public void setRoverml_block(roverml_Block roverml_block) {
        this.roverml_block = roverml_block;
    }
    public List<roverml_Component> getRoverml_components() {
        return roverml_components;
    }

    public void addRoverml_component(Roverml_component roverml_component) {
        this.roverml_components.add(roverml_component);
    }
    public roverml_Transition getRoverml_transition() {
        return roverml_transition;
    }

    public void setRoverml_transition(roverml_Transition roverml_transition) {
        this.roverml_transition = roverml_transition;
    }
    public List<roverml_Transition> getRoverml_transitions() {
        return roverml_transitions;
    }

    public void addRoverml_transition(Roverml_transition roverml_transition) {
        this.roverml_transitions.add(roverml_transition);
    }
    public roverml_Transition getRoverml_transition() {
        return roverml_transition;
    }

    public void setRoverml_transition(roverml_Transition roverml_transition) {
        this.roverml_transition = roverml_transition;
    }

}