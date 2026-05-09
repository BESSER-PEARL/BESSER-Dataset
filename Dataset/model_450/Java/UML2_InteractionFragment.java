





import java.util.List;
import java.util.ArrayList;

public class UML2_InteractionFragment extends NamedElement {






    private UML2_InteractionOperand uml2_interactionoperand;




    private UML2_Interaction uml2_interaction;




    private UML2_Lifeline uml2_lifeline;




    private UML2_Interaction uml2_interaction;




    private UML2_InteractionOperand uml2_interactionoperand;




    private List<UML2_Lifeline> uml2_lifelines;


    public UML2_InteractionFragment(
    ) {
        super(
        );
        this.uml2_lifelines = new ArrayList<>();
    }

    public UML2_InteractionFragment(
        ArrayList<UML2_Lifeline> uml2_lifelines    ) {
        this.uml2_lifelines = uml2_lifelines;
    }


    public UML2_InteractionOperand getUml2_interactionoperand() {
        return uml2_interactionoperand;
    }

    public void setUml2_interactionoperand(UML2_InteractionOperand uml2_interactionoperand) {
        this.uml2_interactionoperand = uml2_interactionoperand;
    }
    public UML2_Interaction getUml2_interaction() {
        return uml2_interaction;
    }

    public void setUml2_interaction(UML2_Interaction uml2_interaction) {
        this.uml2_interaction = uml2_interaction;
    }
    public UML2_Lifeline getUml2_lifeline() {
        return uml2_lifeline;
    }

    public void setUml2_lifeline(UML2_Lifeline uml2_lifeline) {
        this.uml2_lifeline = uml2_lifeline;
    }
    public UML2_Interaction getUml2_interaction() {
        return uml2_interaction;
    }

    public void setUml2_interaction(UML2_Interaction uml2_interaction) {
        this.uml2_interaction = uml2_interaction;
    }
    public UML2_InteractionOperand getUml2_interactionoperand() {
        return uml2_interactionoperand;
    }

    public void setUml2_interactionoperand(UML2_InteractionOperand uml2_interactionoperand) {
        this.uml2_interactionoperand = uml2_interactionoperand;
    }
    public List<UML2_Lifeline> getUml2_lifelines() {
        return uml2_lifelines;
    }

    public void addUml2_lifeline(Uml2_lifeline uml2_lifeline) {
        this.uml2_lifelines.add(uml2_lifeline);
    }

}