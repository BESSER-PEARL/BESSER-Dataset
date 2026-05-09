





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_CombinedFragment  {

    private String interactionOperator;





    private CompleteDSLPckg_InteractionOperand completedslpckg_interactionoperand;




    private List<CompleteDSLPckg_Gate> completedslpckg_gates;


    public CompleteDSLPckg_CombinedFragment(
        String interactionOperator    ) {
        this.interactionOperator = interactionOperator;
        this.completedslpckg_gates = new ArrayList<>();
    }

    public CompleteDSLPckg_CombinedFragment(
        String interactionOperator        ArrayList<CompleteDSLPckg_Gate> completedslpckg_gates    ) {
        this.interactionOperator = interactionOperator;
        this.completedslpckg_gates = completedslpckg_gates;
    }

    public String getInteractionoperator() {
        return interactionOperator;
    }

    public void setInteractionoperator(String interactionOperator) {
        this.interactionOperator = interactionOperator;
    }

    public CompleteDSLPckg_InteractionOperand getCompletedslpckg_interactionoperand() {
        return completedslpckg_interactionoperand;
    }

    public void setCompletedslpckg_interactionoperand(CompleteDSLPckg_InteractionOperand completedslpckg_interactionoperand) {
        this.completedslpckg_interactionoperand = completedslpckg_interactionoperand;
    }
    public List<CompleteDSLPckg_Gate> getCompletedslpckg_gates() {
        return completedslpckg_gates;
    }

    public void addCompletedslpckg_gate(Completedslpckg_gate completedslpckg_gate) {
        this.completedslpckg_gates.add(completedslpckg_gate);
    }

}