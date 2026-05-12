





import java.util.List;
import java.util.ArrayList;

public class lit_petriNets_Transition  {

    private String name;





    private List<lit_petriNets_TPArc> lit_petrinets_tparcs;




    private List<lit_petriNets_PTArc> lit_petrinets_ptarcs;




    private lit_petriNets_Net lit_petrinets_net;




    private lit_petriNets_Net lit_petrinets_net;




    private lit_petriNets_PTArc lit_petrinets_ptarc;




    private lit_petriNets_TPArc lit_petrinets_tparc;


    public lit_petriNets_Transition(
        String name    ) {
        this.name = name;
        this.lit_petrinets_tparcs = new ArrayList<>();
        this.lit_petrinets_ptarcs = new ArrayList<>();
    }

    public lit_petriNets_Transition(
        String name        ArrayList<lit_petriNets_TPArc> lit_petrinets_tparcs,        ArrayList<lit_petriNets_PTArc> lit_petrinets_ptarcs    ) {
        this.name = name;
        this.lit_petrinets_tparcs = lit_petrinets_tparcs;
        this.lit_petrinets_ptarcs = lit_petrinets_ptarcs;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<lit_petriNets_TPArc> getLit_petrinets_tparcs() {
        return lit_petrinets_tparcs;
    }

    public void addLit_petrinets_tparc(Lit_petrinets_tparc lit_petrinets_tparc) {
        this.lit_petrinets_tparcs.add(lit_petrinets_tparc);
    }
    public List<lit_petriNets_PTArc> getLit_petrinets_ptarcs() {
        return lit_petrinets_ptarcs;
    }

    public void addLit_petrinets_ptarc(Lit_petrinets_ptarc lit_petrinets_ptarc) {
        this.lit_petrinets_ptarcs.add(lit_petrinets_ptarc);
    }
    public lit_petriNets_Net getLit_petrinets_net() {
        return lit_petrinets_net;
    }

    public void setLit_petrinets_net(lit_petriNets_Net lit_petrinets_net) {
        this.lit_petrinets_net = lit_petrinets_net;
    }
    public lit_petriNets_Net getLit_petrinets_net() {
        return lit_petrinets_net;
    }

    public void setLit_petrinets_net(lit_petriNets_Net lit_petrinets_net) {
        this.lit_petrinets_net = lit_petrinets_net;
    }
    public lit_petriNets_PTArc getLit_petrinets_ptarc() {
        return lit_petrinets_ptarc;
    }

    public void setLit_petrinets_ptarc(lit_petriNets_PTArc lit_petrinets_ptarc) {
        this.lit_petrinets_ptarc = lit_petrinets_ptarc;
    }
    public lit_petriNets_TPArc getLit_petrinets_tparc() {
        return lit_petrinets_tparc;
    }

    public void setLit_petrinets_tparc(lit_petriNets_TPArc lit_petrinets_tparc) {
        this.lit_petrinets_tparc = lit_petrinets_tparc;
    }

}