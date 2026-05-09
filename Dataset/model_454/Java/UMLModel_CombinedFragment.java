





import java.util.List;
import java.util.ArrayList;

public class UMLModel_CombinedFragment extends InteractionFragment {

    private String interactionOperator;





    private List<UMLModel_InteractionOperand> umlmodel_interactionoperands;




    private List<UMLModel_Gate> umlmodel_gates;


    public UMLModel_CombinedFragment(
        String interactionOperator    ) {
        super(
        );
        this.interactionOperator = interactionOperator;
        this.umlmodel_interactionoperands = new ArrayList<>();
        this.umlmodel_gates = new ArrayList<>();
    }

    public UMLModel_CombinedFragment(
        String interactionOperator        ArrayList<UMLModel_InteractionOperand> umlmodel_interactionoperands,        ArrayList<UMLModel_Gate> umlmodel_gates    ) {
        this.interactionOperator = interactionOperator;
        this.umlmodel_interactionoperands = umlmodel_interactionoperands;
        this.umlmodel_gates = umlmodel_gates;
    }

    public String getInteractionoperator() {
        return interactionOperator;
    }

    public void setInteractionoperator(String interactionOperator) {
        this.interactionOperator = interactionOperator;
    }

    public List<UMLModel_InteractionOperand> getUmlmodel_interactionoperands() {
        return umlmodel_interactionoperands;
    }

    public void addUmlmodel_interactionoperand(Umlmodel_interactionoperand umlmodel_interactionoperand) {
        this.umlmodel_interactionoperands.add(umlmodel_interactionoperand);
    }
    public List<UMLModel_Gate> getUmlmodel_gates() {
        return umlmodel_gates;
    }

    public void addUmlmodel_gate(Umlmodel_gate umlmodel_gate) {
        this.umlmodel_gates.add(umlmodel_gate);
    }

}