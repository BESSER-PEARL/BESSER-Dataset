





import java.util.List;
import java.util.ArrayList;

public class uml_CombinedFragment extends InteractionFragment {

    private String interactionOperator;





    private List<uml_InteractionOperand> uml_interactionoperands;




    private List<uml_Gate> uml_gates;


    public uml_CombinedFragment(
        String interactionOperator    ) {
        super(
        );
        this.interactionOperator = interactionOperator;
        this.uml_interactionoperands = new ArrayList<>();
        this.uml_gates = new ArrayList<>();
    }

    public uml_CombinedFragment(
        String interactionOperator        ArrayList<uml_InteractionOperand> uml_interactionoperands,        ArrayList<uml_Gate> uml_gates    ) {
        this.interactionOperator = interactionOperator;
        this.uml_interactionoperands = uml_interactionoperands;
        this.uml_gates = uml_gates;
    }

    public String getInteractionoperator() {
        return interactionOperator;
    }

    public void setInteractionoperator(String interactionOperator) {
        this.interactionOperator = interactionOperator;
    }

    public List<uml_InteractionOperand> getUml_interactionoperands() {
        return uml_interactionoperands;
    }

    public void addUml_interactionoperand(Uml_interactionoperand uml_interactionoperand) {
        this.uml_interactionoperands.add(uml_interactionoperand);
    }
    public List<uml_Gate> getUml_gates() {
        return uml_gates;
    }

    public void addUml_gate(Uml_gate uml_gate) {
        this.uml_gates.add(uml_gate);
    }

}