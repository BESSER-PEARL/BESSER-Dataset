





import java.util.List;
import java.util.ArrayList;

public class pETRI_Arc extends PetriNetElement {

    private boolean readOnly;
    private int multiplicity;





    private pETRI_Node petri_node;




    private pETRI_Node petri_node;


    public pETRI_Arc(
        boolean readOnly,        int multiplicity    ) {
        super(
        );
        this.readOnly = readOnly;
        this.multiplicity = multiplicity;
    }


    public boolean getReadonly() {
        return readOnly;
    }

    public void setReadonly(boolean readOnly) {
        this.readOnly = readOnly;
    }
    public int getMultiplicity() {
        return multiplicity;
    }

    public void setMultiplicity(int multiplicity) {
        this.multiplicity = multiplicity;
    }

    public pETRI_Node getPetri_node() {
        return petri_node;
    }

    public void setPetri_node(pETRI_Node petri_node) {
        this.petri_node = petri_node;
    }
    public pETRI_Node getPetri_node() {
        return petri_node;
    }

    public void setPetri_node(pETRI_Node petri_node) {
        this.petri_node = petri_node;
    }

}