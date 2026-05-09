





import java.util.List;
import java.util.ArrayList;

public class lit_petriNets_2_Transition  {

    private String name;





    private lit_petriNets_2_Net lit_petrinets_2_net;




    private lit_petriNets_2_Net lit_petrinets_2_net;




    private List<lit_petriNets_2_TPArc> lit_petrinets_2_tparcs;




    private lit_petriNets_2_PTArc lit_petrinets_2_ptarc;




    private List<lit_petriNets_2_PTArc> lit_petrinets_2_ptarcs;




    private lit_petriNets_2_TPArc lit_petrinets_2_tparc;


    public lit_petriNets_2_Transition(
        String name    ) {
        this.name = name;
        this.lit_petrinets_2_tparcs = new ArrayList<>();
        this.lit_petrinets_2_ptarcs = new ArrayList<>();
    }

    public lit_petriNets_2_Transition(
        String name        ArrayList<lit_petriNets_2_TPArc> lit_petrinets_2_tparcs,        ArrayList<lit_petriNets_2_PTArc> lit_petrinets_2_ptarcs    ) {
        this.name = name;
        this.lit_petrinets_2_tparcs = lit_petrinets_2_tparcs;
        this.lit_petrinets_2_ptarcs = lit_petrinets_2_ptarcs;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public lit_petriNets_2_Net getLit_petrinets_2_net() {
        return lit_petrinets_2_net;
    }

    public void setLit_petrinets_2_net(lit_petriNets_2_Net lit_petrinets_2_net) {
        this.lit_petrinets_2_net = lit_petrinets_2_net;
    }
    public lit_petriNets_2_Net getLit_petrinets_2_net() {
        return lit_petrinets_2_net;
    }

    public void setLit_petrinets_2_net(lit_petriNets_2_Net lit_petrinets_2_net) {
        this.lit_petrinets_2_net = lit_petrinets_2_net;
    }
    public List<lit_petriNets_2_TPArc> getLit_petrinets_2_tparcs() {
        return lit_petrinets_2_tparcs;
    }

    public void addLit_petrinets_2_tparc(Lit_petrinets_2_tparc lit_petrinets_2_tparc) {
        this.lit_petrinets_2_tparcs.add(lit_petrinets_2_tparc);
    }
    public lit_petriNets_2_PTArc getLit_petrinets_2_ptarc() {
        return lit_petrinets_2_ptarc;
    }

    public void setLit_petrinets_2_ptarc(lit_petriNets_2_PTArc lit_petrinets_2_ptarc) {
        this.lit_petrinets_2_ptarc = lit_petrinets_2_ptarc;
    }
    public List<lit_petriNets_2_PTArc> getLit_petrinets_2_ptarcs() {
        return lit_petrinets_2_ptarcs;
    }

    public void addLit_petrinets_2_ptarc(Lit_petrinets_2_ptarc lit_petrinets_2_ptarc) {
        this.lit_petrinets_2_ptarcs.add(lit_petrinets_2_ptarc);
    }
    public lit_petriNets_2_TPArc getLit_petrinets_2_tparc() {
        return lit_petrinets_2_tparc;
    }

    public void setLit_petrinets_2_tparc(lit_petriNets_2_TPArc lit_petrinets_2_tparc) {
        this.lit_petrinets_2_tparc = lit_petrinets_2_tparc;
    }

}