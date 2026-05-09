





import java.util.List;
import java.util.ArrayList;

public class ocl_ecore_Constraint extends ENamedElement {

    private String stereotype;



    public ocl_ecore_Constraint(
        String stereotype    ) {
        super(
        );
        this.stereotype = stereotype;
    }


    public String getStereotype() {
        return stereotype;
    }

    public void setStereotype(String stereotype) {
        this.stereotype = stereotype;
    }


}