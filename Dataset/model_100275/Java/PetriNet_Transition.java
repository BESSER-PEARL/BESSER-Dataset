





import java.util.List;
import java.util.ArrayList;

public class PetriNet_Transition  {






    private List<TPArc> tparcs;




    private List<PTArc> ptarcs;




    private Net net;


    public PetriNet_Transition(
    ) {
        this.tparcs = new ArrayList<>();
        this.ptarcs = new ArrayList<>();
    }

    public PetriNet_Transition(
        ArrayList<TPArc> tparcs,        ArrayList<PTArc> ptarcs    ) {
        this.tparcs = tparcs;
        this.ptarcs = ptarcs;
    }


    public List<TPArc> getTparcs() {
        return tparcs;
    }

    public void addTparc(Tparc tparc) {
        this.tparcs.add(tparc);
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

}