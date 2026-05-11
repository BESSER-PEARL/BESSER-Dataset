





import java.util.List;
import java.util.ArrayList;

public class dsml_DContainment extends DContainedEdge {

    private boolean compartment;



    public dsml_DContainment(
        boolean compartment    ) {
        super(
        );
        this.compartment = compartment;
    }


    public boolean getCompartment() {
        return compartment;
    }

    public void setCompartment(boolean compartment) {
        this.compartment = compartment;
    }


}