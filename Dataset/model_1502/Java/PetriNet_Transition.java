





import java.util.List;
import java.util.ArrayList;

public class PetriNet_Transition extends PetriNode {






    private PetriNet_PetriNode petrinet_petrinode;


    public PetriNet_Transition(
    ) {
        super(
        );
    }



    public PetriNet_PetriNode getPetrinet_petrinode() {
        return petrinet_petrinode;
    }

    public void setPetrinet_petrinode(PetriNet_PetriNode petrinet_petrinode) {
        this.petrinet_petrinode = petrinet_petrinode;
    }

}