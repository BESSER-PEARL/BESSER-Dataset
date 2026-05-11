





import java.util.List;
import java.util.ArrayList;

public class ram_CombinedFragment extends InteractionFragment {

    private String interactionOperator;





    private List<ram_InteractionOperand> ram_interactionoperands;


    public ram_CombinedFragment(
        String interactionOperator    ) {
        super(
        );
        this.interactionOperator = interactionOperator;
        this.ram_interactionoperands = new ArrayList<>();
    }

    public ram_CombinedFragment(
        String interactionOperator        ArrayList<ram_InteractionOperand> ram_interactionoperands    ) {
        this.interactionOperator = interactionOperator;
        this.ram_interactionoperands = ram_interactionoperands;
    }

    public String getInteractionoperator() {
        return interactionOperator;
    }

    public void setInteractionoperator(String interactionOperator) {
        this.interactionOperator = interactionOperator;
    }

    public List<ram_InteractionOperand> getRam_interactionoperands() {
        return ram_interactionoperands;
    }

    public void addRam_interactionoperand(Ram_interactionoperand ram_interactionoperand) {
        this.ram_interactionoperands.add(ram_interactionoperand);
    }

}