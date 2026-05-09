





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_Lifeline extends NamedElement {






    private UML2WithID_InteractionFragment uml2withid_interactionfragment;




    private UML2WithID_ConnectableElement uml2withid_connectableelement;




    private List<UML2WithID_InteractionFragment> uml2withid_interactionfragments;


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


    public UML2WithID_InteractionFragment getUml2withid_interactionfragment() {
        return uml2withid_interactionfragment;
    }

    public void setUml2withid_interactionfragment(UML2WithID_InteractionFragment uml2withid_interactionfragment) {
        this.uml2withid_interactionfragment = uml2withid_interactionfragment;
    }
    public UML2WithID_ConnectableElement getUml2withid_connectableelement() {
        return uml2withid_connectableelement;
    }

    public void setUml2withid_connectableelement(UML2WithID_ConnectableElement uml2withid_connectableelement) {
        this.uml2withid_connectableelement = uml2withid_connectableelement;
    }
    public List<UML2WithID_InteractionFragment> getUml2withid_interactionfragments() {
        return uml2withid_interactionfragments;
    }

    public void addUml2withid_interactionfragment(Uml2withid_interactionfragment uml2withid_interactionfragment) {
        this.uml2withid_interactionfragments.add(uml2withid_interactionfragment);
    }

}