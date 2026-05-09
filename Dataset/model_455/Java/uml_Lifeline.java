





import java.util.List;
import java.util.ArrayList;

public class uml_Lifeline extends NamedElement {






    private List<uml_InteractionFragment> uml_interactionfragments;




    private uml_InteractionFragment uml_interactionfragment;




    private uml_ValueSpecification uml_valuespecification;


    public uml_Lifeline(
    ) {
        super(
        );
        this.uml_interactionfragments = new ArrayList<>();
    }

    public uml_Lifeline(
        ArrayList<uml_InteractionFragment> uml_interactionfragments    ) {
        this.uml_interactionfragments = uml_interactionfragments;
    }


    public List<uml_InteractionFragment> getUml_interactionfragments() {
        return uml_interactionfragments;
    }

    public void addUml_interactionfragment(Uml_interactionfragment uml_interactionfragment) {
        this.uml_interactionfragments.add(uml_interactionfragment);
    }
    public uml_InteractionFragment getUml_interactionfragment() {
        return uml_interactionfragment;
    }

    public void setUml_interactionfragment(uml_InteractionFragment uml_interactionfragment) {
        this.uml_interactionfragment = uml_interactionfragment;
    }
    public uml_ValueSpecification getUml_valuespecification() {
        return uml_valuespecification;
    }

    public void setUml_valuespecification(uml_ValueSpecification uml_valuespecification) {
        this.uml_valuespecification = uml_valuespecification;
    }

}