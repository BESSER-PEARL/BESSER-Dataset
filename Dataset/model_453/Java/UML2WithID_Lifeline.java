





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_Lifeline extends NamedElement {






    private UML2WithID_Interaction uml2withid_interaction;




    private UML2WithID_Interaction uml2withid_interaction;




    private UML2WithID_OpaqueExpression uml2withid_opaqueexpression;




    private List<UML2WithID_InteractionFragment> uml2withid_interactionfragments;




    private UML2WithID_ConnectableElement uml2withid_connectableelement;




    private UML2WithID_InteractionFragment uml2withid_interactionfragment;


    public UML2WithID_Lifeline(
    ) {
        super(
        );
        this.uml2withid_interactionfragments = new ArrayList<>();
    }

    public UML2WithID_Lifeline(
        ArrayList<UML2WithID_InteractionFragment> uml2withid_interactionfragments    ) {
        this.uml2withid_interactionfragments = uml2withid_interactionfragments;
    }


    public UML2WithID_Interaction getUml2withid_interaction() {
        return uml2withid_interaction;
    }

    public void setUml2withid_interaction(UML2WithID_Interaction uml2withid_interaction) {
        this.uml2withid_interaction = uml2withid_interaction;
    }
    public UML2WithID_Interaction getUml2withid_interaction() {
        return uml2withid_interaction;
    }

    public void setUml2withid_interaction(UML2WithID_Interaction uml2withid_interaction) {
        this.uml2withid_interaction = uml2withid_interaction;
    }
    public UML2WithID_OpaqueExpression getUml2withid_opaqueexpression() {
        return uml2withid_opaqueexpression;
    }

    public void setUml2withid_opaqueexpression(UML2WithID_OpaqueExpression uml2withid_opaqueexpression) {
        this.uml2withid_opaqueexpression = uml2withid_opaqueexpression;
    }
    public List<UML2WithID_InteractionFragment> getUml2withid_interactionfragments() {
        return uml2withid_interactionfragments;
    }

    public void addUml2withid_interactionfragment(Uml2withid_interactionfragment uml2withid_interactionfragment) {
        this.uml2withid_interactionfragments.add(uml2withid_interactionfragment);
    }
    public UML2WithID_ConnectableElement getUml2withid_connectableelement() {
        return uml2withid_connectableelement;
    }

    public void setUml2withid_connectableelement(UML2WithID_ConnectableElement uml2withid_connectableelement) {
        this.uml2withid_connectableelement = uml2withid_connectableelement;
    }
    public UML2WithID_InteractionFragment getUml2withid_interactionfragment() {
        return uml2withid_interactionfragment;
    }

    public void setUml2withid_interactionfragment(UML2WithID_InteractionFragment uml2withid_interactionfragment) {
        this.uml2withid_interactionfragment = uml2withid_interactionfragment;
    }

}