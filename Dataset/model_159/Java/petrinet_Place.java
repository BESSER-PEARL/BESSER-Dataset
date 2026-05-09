





import java.util.List;
import java.util.ArrayList;

public class petrinet_Place  {

    private String name;





    private petrinet_Petrinet petrinet_petrinet;




    private List<petrinet_TPArc> petrinet_tparcs;




    private petrinet_TPArc petrinet_tparc;


    public petrinet_Place(
        String name    ) {
        this.name = name;
        this.petrinet_tparcs = new ArrayList<>();
    }

    public petrinet_Place(
        String name        ArrayList<petrinet_TPArc> petrinet_tparcs    ) {
        this.name = name;
        this.petrinet_tparcs = petrinet_tparcs;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public petrinet_Petrinet getPetrinet_petrinet() {
        return petrinet_petrinet;
    }

    public void setPetrinet_petrinet(petrinet_Petrinet petrinet_petrinet) {
        this.petrinet_petrinet = petrinet_petrinet;
    }
    public List<petrinet_TPArc> getPetrinet_tparcs() {
        return petrinet_tparcs;
    }

    public void addPetrinet_tparc(Petrinet_tparc petrinet_tparc) {
        this.petrinet_tparcs.add(petrinet_tparc);
    }
    public petrinet_TPArc getPetrinet_tparc() {
        return petrinet_tparc;
    }

    public void setPetrinet_tparc(petrinet_TPArc petrinet_tparc) {
        this.petrinet_tparc = petrinet_tparc;
    }

}