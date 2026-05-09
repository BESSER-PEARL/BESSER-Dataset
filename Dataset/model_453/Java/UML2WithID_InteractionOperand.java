





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_InteractionOperand extends InteractionFragment, Namespace {






    private List<UML2WithID_InteractionFragment> uml2withid_interactionfragments;




    private UML2WithID_InteractionFragment uml2withid_interactionfragment;


    public UML2WithID_InteractionOperand(
    ) {
        super(
        );
        this.uml2withid_interactionfragments = new ArrayList<>();
    }

    public UML2WithID_InteractionOperand(
        ArrayList<UML2WithID_InteractionFragment> uml2withid_interactionfragments    ) {
        this.uml2withid_interactionfragments = uml2withid_interactionfragments;
    }


    public List<UML2WithID_InteractionFragment> getUml2withid_interactionfragments() {
        return uml2withid_interactionfragments;
    }

    public void addUml2withid_interactionfragment(Uml2withid_interactionfragment uml2withid_interactionfragment) {
        this.uml2withid_interactionfragments.add(uml2withid_interactionfragment);
    }
    public UML2WithID_InteractionFragment getUml2withid_interactionfragment() {
        return uml2withid_interactionfragment;
    }

    public void setUml2withid_interactionfragment(UML2WithID_InteractionFragment uml2withid_interactionfragment) {
        this.uml2withid_interactionfragment = uml2withid_interactionfragment;
    }

}