





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedCombinedFragment extends TracedInteractionFragment {






    private List<uml_TracedInteractionOperand> uml_tracedinteractionoperands;




    private List<uml_TracedGate> uml_tracedgates;


    public umlTrace_uml_TracedCombinedFragment(
    ) {
        super(
        );
        this.uml_tracedinteractionoperands = new ArrayList<>();
        this.uml_tracedgates = new ArrayList<>();
    }

    public umlTrace_uml_TracedCombinedFragment(
        ArrayList<uml_TracedInteractionOperand> uml_tracedinteractionoperands,        ArrayList<uml_TracedGate> uml_tracedgates    ) {
        this.uml_tracedinteractionoperands = uml_tracedinteractionoperands;
        this.uml_tracedgates = uml_tracedgates;
    }


    public List<uml_TracedInteractionOperand> getUml_tracedinteractionoperands() {
        return uml_tracedinteractionoperands;
    }

    public void addUml_tracedinteractionoperand(Uml_tracedinteractionoperand uml_tracedinteractionoperand) {
        this.uml_tracedinteractionoperands.add(uml_tracedinteractionoperand);
    }
    public List<uml_TracedGate> getUml_tracedgates() {
        return uml_tracedgates;
    }

    public void addUml_tracedgate(Uml_tracedgate uml_tracedgate) {
        this.uml_tracedgates.add(uml_tracedgate);
    }

}