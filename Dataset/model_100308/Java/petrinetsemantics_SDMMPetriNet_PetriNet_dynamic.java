





import java.util.List;
import java.util.ArrayList;

public class petrinetsemantics_SDMMPetriNet_PetriNet_dynamic  {






    private List<Node_dynamic> node_dynamics;




    private PetriNet petrinet;


    public petrinetsemantics_SDMMPetriNet_PetriNet_dynamic(
    ) {
        this.node_dynamics = new ArrayList<>();
    }

    public petrinetsemantics_SDMMPetriNet_PetriNet_dynamic(
        ArrayList<Node_dynamic> node_dynamics    ) {
        this.node_dynamics = node_dynamics;
    }


    public List<Node_dynamic> getNode_dynamics() {
        return node_dynamics;
    }

    public void addNode_dynamic(Node_dynamic node_dynamic) {
        this.node_dynamics.add(node_dynamic);
    }
    public PetriNet getPetrinet() {
        return petrinet;
    }

    public void setPetrinet(PetriNet petrinet) {
        this.petrinet = petrinet;
    }

}