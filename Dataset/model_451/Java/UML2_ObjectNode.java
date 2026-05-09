





import java.util.List;
import java.util.ArrayList;

public class UML2_ObjectNode extends ActivityNode, TypedElement {

    private String ordering;





    private UML2_ValueSpecification uml2_valuespecification;




    private UML2_Behavior uml2_behavior;


    public UML2_ObjectNode(
        String ordering    ) {
        super(
        );
        this.ordering = ordering;
    }


    public String getOrdering() {
        return ordering;
    }

    public void setOrdering(String ordering) {
        this.ordering = ordering;
    }

    public UML2_ValueSpecification getUml2_valuespecification() {
        return uml2_valuespecification;
    }

    public void setUml2_valuespecification(UML2_ValueSpecification uml2_valuespecification) {
        this.uml2_valuespecification = uml2_valuespecification;
    }
    public UML2_Behavior getUml2_behavior() {
        return uml2_behavior;
    }

    public void setUml2_behavior(UML2_Behavior uml2_behavior) {
        this.uml2_behavior = uml2_behavior;
    }

}