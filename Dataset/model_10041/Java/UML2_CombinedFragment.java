





import java.util.List;
import java.util.ArrayList;

public class UML2_CombinedFragment extends InteractionFragment {

    private String interactionOperator;





    private List<UML2_InteractionOperand> uml2_interactionoperands;


    public UML2_CombinedFragment(
        String interactionOperator    ) {
        super(
        );
        this.interactionOperator = interactionOperator;
        this.uml2_interactionoperands = new ArrayList<>();
    }

    public UML2_CombinedFragment(
        String interactionOperator        ArrayList<UML2_InteractionOperand> uml2_interactionoperands    ) {
        this.interactionOperator = interactionOperator;
        this.uml2_interactionoperands = uml2_interactionoperands;
    }

    public String getInteractionoperator() {
        return interactionOperator;
    }

    public void setInteractionoperator(String interactionOperator) {
        this.interactionOperator = interactionOperator;
    }

    public List<UML2_InteractionOperand> getUml2_interactionoperands() {
        return uml2_interactionoperands;
    }

    public void addUml2_interactionoperand(Uml2_interactionoperand uml2_interactionoperand) {
        this.uml2_interactionoperands.add(uml2_interactionoperand);
    }

}