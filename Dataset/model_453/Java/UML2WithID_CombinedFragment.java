





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_CombinedFragment extends InteractionFragment {

    private String interactionOperator;





    private List<UML2WithID_InteractionOperand> uml2withid_interactionoperands;


    public UML2WithID_CombinedFragment(
        String interactionOperator    ) {
        super(
        );
        this.interactionOperator = interactionOperator;
        this.uml2withid_interactionoperands = new ArrayList<>();
    }

    public UML2WithID_CombinedFragment(
        String interactionOperator        ArrayList<UML2WithID_InteractionOperand> uml2withid_interactionoperands    ) {
        this.interactionOperator = interactionOperator;
        this.uml2withid_interactionoperands = uml2withid_interactionoperands;
    }

    public String getInteractionoperator() {
        return interactionOperator;
    }

    public void setInteractionoperator(String interactionOperator) {
        this.interactionOperator = interactionOperator;
    }

    public List<UML2WithID_InteractionOperand> getUml2withid_interactionoperands() {
        return uml2withid_interactionoperands;
    }

    public void addUml2withid_interactionoperand(Uml2withid_interactionoperand uml2withid_interactionoperand) {
        this.uml2withid_interactionoperands.add(uml2withid_interactionoperand);
    }

}