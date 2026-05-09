





import java.util.List;
import java.util.ArrayList;

public class petrinet_Transition  {

    private String name;





    private List<petrinet_TPArc> petrinet_tparcs;




    private List<petrinet_PTArc> petrinet_ptarcs;




    private petrinet_TPArc petrinet_tparc;




    private petrinet_PTArc petrinet_ptarc;




    private petrinet_Petrinet petrinet_petrinet;


    public petrinet_Transition(
        String name    ) {
        this.name = name;
        this.petrinet_tparcs = new ArrayList<>();
        this.petrinet_ptarcs = new ArrayList<>();
    }

    public petrinet_Transition(
        String name        ArrayList<petrinet_TPArc> petrinet_tparcs,        ArrayList<petrinet_PTArc> petrinet_ptarcs    ) {
        this.name = name;
        this.petrinet_tparcs = petrinet_tparcs;
        this.petrinet_ptarcs = petrinet_ptarcs;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<petrinet_TPArc> getPetrinet_tparcs() {
        return petrinet_tparcs;
    }

    public void addPetrinet_tparc(Petrinet_tparc petrinet_tparc) {
        this.petrinet_tparcs.add(petrinet_tparc);
    }
    public List<petrinet_PTArc> getPetrinet_ptarcs() {
        return petrinet_ptarcs;
    }

    public void addPetrinet_ptarc(Petrinet_ptarc petrinet_ptarc) {
        this.petrinet_ptarcs.add(petrinet_ptarc);
    }
    public petrinet_TPArc getPetrinet_tparc() {
        return petrinet_tparc;
    }

    public void setPetrinet_tparc(petrinet_TPArc petrinet_tparc) {
        this.petrinet_tparc = petrinet_tparc;
    }
    public petrinet_PTArc getPetrinet_ptarc() {
        return petrinet_ptarc;
    }

    public void setPetrinet_ptarc(petrinet_PTArc petrinet_ptarc) {
        this.petrinet_ptarc = petrinet_ptarc;
    }
    public petrinet_Petrinet getPetrinet_petrinet() {
        return petrinet_petrinet;
    }

    public void setPetrinet_petrinet(petrinet_Petrinet petrinet_petrinet) {
        this.petrinet_petrinet = petrinet_petrinet;
    }

}