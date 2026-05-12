





import java.util.List;
import java.util.ArrayList;

public class PetriNet_Transition  {






    private PetriNet_TPArc petrinet_tparc;




    private List<PetriNet_TPArc> petrinet_tparcs;


    public PetriNet_Transition(
    ) {
        this.petrinet_tparcs = new ArrayList<>();
    }

    public PetriNet_Transition(
        ArrayList<PetriNet_TPArc> petrinet_tparcs    ) {
        this.petrinet_tparcs = petrinet_tparcs;
    }


    public PetriNet_TPArc getPetrinet_tparc() {
        return petrinet_tparc;
    }

    public void setPetrinet_tparc(PetriNet_TPArc petrinet_tparc) {
        this.petrinet_tparc = petrinet_tparc;
    }
    public List<PetriNet_TPArc> getPetrinet_tparcs() {
        return petrinet_tparcs;
    }

    public void addPetrinet_tparc(Petrinet_tparc petrinet_tparc) {
        this.petrinet_tparcs.add(petrinet_tparc);
    }

}