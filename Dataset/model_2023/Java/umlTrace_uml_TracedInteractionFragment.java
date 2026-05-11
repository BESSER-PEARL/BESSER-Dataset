





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedInteractionFragment extends TracedNamedElement {






    private List<uml_TracedLifeline> uml_tracedlifelines;




    private List<uml_TracedGeneralOrdering> uml_tracedgeneralorderings;




    private uml_TracedInteraction uml_tracedinteraction;




    private uml_TracedInteractionOperand uml_tracedinteractionoperand;


    public umlTrace_uml_TracedInteractionFragment(
    ) {
        super(
        );
        this.uml_tracedlifelines = new ArrayList<>();
        this.uml_tracedgeneralorderings = new ArrayList<>();
    }

    public umlTrace_uml_TracedInteractionFragment(
        ArrayList<uml_TracedLifeline> uml_tracedlifelines,        ArrayList<uml_TracedGeneralOrdering> uml_tracedgeneralorderings    ) {
        this.uml_tracedlifelines = uml_tracedlifelines;
        this.uml_tracedgeneralorderings = uml_tracedgeneralorderings;
    }


    public List<uml_TracedLifeline> getUml_tracedlifelines() {
        return uml_tracedlifelines;
    }

    public void addUml_tracedlifeline(Uml_tracedlifeline uml_tracedlifeline) {
        this.uml_tracedlifelines.add(uml_tracedlifeline);
    }
    public List<uml_TracedGeneralOrdering> getUml_tracedgeneralorderings() {
        return uml_tracedgeneralorderings;
    }

    public void addUml_tracedgeneralordering(Uml_tracedgeneralordering uml_tracedgeneralordering) {
        this.uml_tracedgeneralorderings.add(uml_tracedgeneralordering);
    }
    public uml_TracedInteraction getUml_tracedinteraction() {
        return uml_tracedinteraction;
    }

    public void setUml_tracedinteraction(uml_TracedInteraction uml_tracedinteraction) {
        this.uml_tracedinteraction = uml_tracedinteraction;
    }
    public uml_TracedInteractionOperand getUml_tracedinteractionoperand() {
        return uml_tracedinteractionoperand;
    }

    public void setUml_tracedinteractionoperand(uml_TracedInteractionOperand uml_tracedinteractionoperand) {
        this.uml_tracedinteractionoperand = uml_tracedinteractionoperand;
    }

}