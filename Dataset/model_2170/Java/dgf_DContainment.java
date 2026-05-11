





import java.util.List;
import java.util.ArrayList;

public class dgf_DContainment extends DContainedVertex {

    private String compartment;



    public dgf_DContainment(
        String compartment    ) {
        super(
        );
        this.compartment = compartment;
    }


    public String getCompartment() {
        return compartment;
    }

    public void setCompartment(String compartment) {
        this.compartment = compartment;
    }


}