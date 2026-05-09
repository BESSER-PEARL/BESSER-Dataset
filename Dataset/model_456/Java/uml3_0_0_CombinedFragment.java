





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_CombinedFragment extends InteractionFragment {

    private String interactionOperator;





    private List<uml3_0_0_Gate> uml3_0_0_gates;




    private List<uml3_0_0_InteractionOperand> uml3_0_0_interactionoperands;


    public uml3_0_0_CombinedFragment(
        String interactionOperator    ) {
        super(
        );
        this.interactionOperator = interactionOperator;
        this.uml3_0_0_gates = new ArrayList<>();
        this.uml3_0_0_interactionoperands = new ArrayList<>();
    }

    public uml3_0_0_CombinedFragment(
        String interactionOperator        ArrayList<uml3_0_0_Gate> uml3_0_0_gates,        ArrayList<uml3_0_0_InteractionOperand> uml3_0_0_interactionoperands    ) {
        this.interactionOperator = interactionOperator;
        this.uml3_0_0_gates = uml3_0_0_gates;
        this.uml3_0_0_interactionoperands = uml3_0_0_interactionoperands;
    }

    public String getInteractionoperator() {
        return interactionOperator;
    }

    public void setInteractionoperator(String interactionOperator) {
        this.interactionOperator = interactionOperator;
    }

    public List<uml3_0_0_Gate> getUml3_0_0_gates() {
        return uml3_0_0_gates;
    }

    public void addUml3_0_0_gate(Uml3_0_0_gate uml3_0_0_gate) {
        this.uml3_0_0_gates.add(uml3_0_0_gate);
    }
    public List<uml3_0_0_InteractionOperand> getUml3_0_0_interactionoperands() {
        return uml3_0_0_interactionoperands;
    }

    public void addUml3_0_0_interactionoperand(Uml3_0_0_interactionoperand uml3_0_0_interactionoperand) {
        this.uml3_0_0_interactionoperands.add(uml3_0_0_interactionoperand);
    }

}