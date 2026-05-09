





import java.util.List;
import java.util.ArrayList;

public class resourcePetriNet_PetriNet  {

    private String name;





    private List<resourcePetriNet_OutputArc> resourcepetrinet_outputarcs;




    private List<resourcePetriNet_Transition> resourcepetrinet_transitions;




    private List<resourcePetriNet_InputArc> resourcepetrinet_inputarcs;


    public resourcePetriNet_PetriNet(
        String name    ) {
        this.name = name;
        this.resourcepetrinet_outputarcs = new ArrayList<>();
        this.resourcepetrinet_transitions = new ArrayList<>();
        this.resourcepetrinet_inputarcs = new ArrayList<>();
    }

    public resourcePetriNet_PetriNet(
        String name        ArrayList<resourcePetriNet_OutputArc> resourcepetrinet_outputarcs,        ArrayList<resourcePetriNet_Transition> resourcepetrinet_transitions,        ArrayList<resourcePetriNet_InputArc> resourcepetrinet_inputarcs    ) {
        this.name = name;
        this.resourcepetrinet_outputarcs = resourcepetrinet_outputarcs;
        this.resourcepetrinet_transitions = resourcepetrinet_transitions;
        this.resourcepetrinet_inputarcs = resourcepetrinet_inputarcs;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<resourcePetriNet_OutputArc> getResourcepetrinet_outputarcs() {
        return resourcepetrinet_outputarcs;
    }

    public void addResourcepetrinet_outputarc(Resourcepetrinet_outputarc resourcepetrinet_outputarc) {
        this.resourcepetrinet_outputarcs.add(resourcepetrinet_outputarc);
    }
    public List<resourcePetriNet_Transition> getResourcepetrinet_transitions() {
        return resourcepetrinet_transitions;
    }

    public void addResourcepetrinet_transition(Resourcepetrinet_transition resourcepetrinet_transition) {
        this.resourcepetrinet_transitions.add(resourcepetrinet_transition);
    }
    public List<resourcePetriNet_InputArc> getResourcepetrinet_inputarcs() {
        return resourcepetrinet_inputarcs;
    }

    public void addResourcepetrinet_inputarc(Resourcepetrinet_inputarc resourcepetrinet_inputarc) {
        this.resourcepetrinet_inputarcs.add(resourcepetrinet_inputarc);
    }

}