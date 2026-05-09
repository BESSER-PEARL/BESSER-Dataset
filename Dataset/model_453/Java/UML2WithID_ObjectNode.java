





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_ObjectNode extends ActivityNode, TypedElement {

    private String ordering;





    private UML2WithID_ValueSpecification uml2withid_valuespecification;




    private UML2WithID_Behavior uml2withid_behavior;




    private UML2WithID_ExceptionHandler uml2withid_exceptionhandler;


    public UML2WithID_ObjectNode(
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

    public UML2WithID_ValueSpecification getUml2withid_valuespecification() {
        return uml2withid_valuespecification;
    }

    public void setUml2withid_valuespecification(UML2WithID_ValueSpecification uml2withid_valuespecification) {
        this.uml2withid_valuespecification = uml2withid_valuespecification;
    }
    public UML2WithID_Behavior getUml2withid_behavior() {
        return uml2withid_behavior;
    }

    public void setUml2withid_behavior(UML2WithID_Behavior uml2withid_behavior) {
        this.uml2withid_behavior = uml2withid_behavior;
    }
    public UML2WithID_ExceptionHandler getUml2withid_exceptionhandler() {
        return uml2withid_exceptionhandler;
    }

    public void setUml2withid_exceptionhandler(UML2WithID_ExceptionHandler uml2withid_exceptionhandler) {
        this.uml2withid_exceptionhandler = uml2withid_exceptionhandler;
    }

}