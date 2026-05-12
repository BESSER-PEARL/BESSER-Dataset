





import java.util.List;
import java.util.ArrayList;

public class PetriNet_Transition  {






    private List<PTArc> ptarcs;




    private Net net;




    private List<TPArc> tparcs;


    public PetriNet_Transition(
    ) {
        this.ptarcs = new ArrayList<>();
        this.tparcs = new ArrayList<>();
    }

    public PetriNet_Transition(
        ArrayList<PTArc> ptarcs,        ArrayList<TPArc> tparcs    ) {
        this.ptarcs = ptarcs;
        this.tparcs = tparcs;
    }


    public List<PTArc> getPtarcs() {
        return ptarcs;
    }

    public void addPtarc(Ptarc ptarc) {
        this.ptarcs.add(ptarc);
    }
    public Net getNet() {
        return net;
    }

    public void setNet(Net net) {
        this.net = net;
    }
    public List<TPArc> getTparcs() {
        return tparcs;
    }

    public void addTparc(Tparc tparc) {
        this.tparcs.add(tparc);
    }

}