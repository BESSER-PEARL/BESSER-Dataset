





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_InteractionFragment extends NamedElement {






    private uml3_0_0_InteractionOperand uml3_0_0_interactionoperand;




    private uml3_0_0_InteractionOperand uml3_0_0_interactionoperand;




    private uml3_0_0_Lifeline uml3_0_0_lifeline;




    private List<uml3_0_0_Lifeline> uml3_0_0_lifelines;


    public uml3_0_0_InteractionFragment(
    ) {
        super(
        );
        this.uml3_0_0_lifelines = new ArrayList<>();
    }

    public uml3_0_0_InteractionFragment(
        ArrayList<uml3_0_0_Lifeline> uml3_0_0_lifelines    ) {
        this.uml3_0_0_lifelines = uml3_0_0_lifelines;
    }


    public uml3_0_0_InteractionOperand getUml3_0_0_interactionoperand() {
        return uml3_0_0_interactionoperand;
    }

    public void setUml3_0_0_interactionoperand(uml3_0_0_InteractionOperand uml3_0_0_interactionoperand) {
        this.uml3_0_0_interactionoperand = uml3_0_0_interactionoperand;
    }
    public uml3_0_0_InteractionOperand getUml3_0_0_interactionoperand() {
        return uml3_0_0_interactionoperand;
    }

    public void setUml3_0_0_interactionoperand(uml3_0_0_InteractionOperand uml3_0_0_interactionoperand) {
        this.uml3_0_0_interactionoperand = uml3_0_0_interactionoperand;
    }
    public uml3_0_0_Lifeline getUml3_0_0_lifeline() {
        return uml3_0_0_lifeline;
    }

    public void setUml3_0_0_lifeline(uml3_0_0_Lifeline uml3_0_0_lifeline) {
        this.uml3_0_0_lifeline = uml3_0_0_lifeline;
    }
    public List<uml3_0_0_Lifeline> getUml3_0_0_lifelines() {
        return uml3_0_0_lifelines;
    }

    public void addUml3_0_0_lifeline(Uml3_0_0_lifeline uml3_0_0_lifeline) {
        this.uml3_0_0_lifelines.add(uml3_0_0_lifeline);
    }

}