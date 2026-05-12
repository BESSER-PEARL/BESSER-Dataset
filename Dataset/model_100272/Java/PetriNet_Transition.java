





import java.util.List;
import java.util.ArrayList;

public class PetriNet_Transition  {






    private PetriNet_Net petrinet_net;




    private List<PetriNet_PTArc> petrinet_ptarcs;




    private PetriNet_TPArc petrinet_tparc;




    private PetriNet_PTArc petrinet_ptarc;




    private List<PetriNet_TPArc> petrinet_tparcs;




    private PetriNet_Net petrinet_net;


    public PetriNet_Transition(
    ) {
        this.petrinet_ptarcs = new ArrayList<>();
        this.petrinet_tparcs = new ArrayList<>();
    }

    public PetriNet_Transition(
        ArrayList<PetriNet_PTArc> petrinet_ptarcs,        ArrayList<PetriNet_TPArc> petrinet_tparcs    ) {
        this.petrinet_ptarcs = petrinet_ptarcs;
        this.petrinet_tparcs = petrinet_tparcs;
    }


    public PetriNet_Net getPetrinet_net() {
        return petrinet_net;
    }

    public void setPetrinet_net(PetriNet_Net petrinet_net) {
        this.petrinet_net = petrinet_net;
    }
    public List<PetriNet_PTArc> getPetrinet_ptarcs() {
        return petrinet_ptarcs;
    }

    public void addPetrinet_ptarc(Petrinet_ptarc petrinet_ptarc) {
        this.petrinet_ptarcs.add(petrinet_ptarc);
    }
    public PetriNet_TPArc getPetrinet_tparc() {
        return petrinet_tparc;
    }

    public void setPetrinet_tparc(PetriNet_TPArc petrinet_tparc) {
        this.petrinet_tparc = petrinet_tparc;
    }
    public PetriNet_PTArc getPetrinet_ptarc() {
        return petrinet_ptarc;
    }

    public void setPetrinet_ptarc(PetriNet_PTArc petrinet_ptarc) {
        this.petrinet_ptarc = petrinet_ptarc;
    }
    public List<PetriNet_TPArc> getPetrinet_tparcs() {
        return petrinet_tparcs;
    }

    public void addPetrinet_tparc(Petrinet_tparc petrinet_tparc) {
        this.petrinet_tparcs.add(petrinet_tparc);
    }
    public PetriNet_Net getPetrinet_net() {
        return petrinet_net;
    }

    public void setPetrinet_net(PetriNet_Net petrinet_net) {
        this.petrinet_net = petrinet_net;
    }

}