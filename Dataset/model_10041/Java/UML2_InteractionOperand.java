





import java.util.List;
import java.util.ArrayList;

public class UML2_InteractionOperand extends Namespace, InteractionFragment {






    private List<UML2_InteractionFragment> uml2_interactionfragments;




    private UML2_InteractionFragment uml2_interactionfragment;


    public UML2_InteractionOperand(
    ) {
        super(
        );
        this.uml2_interactionfragments = new ArrayList<>();
    }

    public UML2_InteractionOperand(
        ArrayList<UML2_InteractionFragment> uml2_interactionfragments    ) {
        this.uml2_interactionfragments = uml2_interactionfragments;
    }


    public List<UML2_InteractionFragment> getUml2_interactionfragments() {
        return uml2_interactionfragments;
    }

    public void addUml2_interactionfragment(Uml2_interactionfragment uml2_interactionfragment) {
        this.uml2_interactionfragments.add(uml2_interactionfragment);
    }
    public UML2_InteractionFragment getUml2_interactionfragment() {
        return uml2_interactionfragment;
    }

    public void setUml2_interactionfragment(UML2_InteractionFragment uml2_interactionfragment) {
        this.uml2_interactionfragment = uml2_interactionfragment;
    }

}