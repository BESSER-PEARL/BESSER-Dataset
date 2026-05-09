





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_ObjectNode extends TypedElement, ActivityNode {

    private String ordering;





    private UML2WithID_ValueSpecification uml2withid_valuespecification;




    private UML2WithID_Behavior uml2withid_behavior;




    private List<UML2WithID_State> uml2withid_states;




    private UML2WithID_ExceptionHandler uml2withid_exceptionhandler;


    public UML2WithID_ObjectNode(
        String ordering    ) {
        super(
        );
        this.ordering = ordering;
        this.uml2withid_states = new ArrayList<>();
    }

    public UML2WithID_ObjectNode(
        String ordering        ArrayList<UML2WithID_State> uml2withid_states    ) {
        this.ordering = ordering;
        this.uml2withid_states = uml2withid_states;
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
    public List<UML2WithID_State> getUml2withid_states() {
        return uml2withid_states;
    }

    public void addUml2withid_state(Uml2withid_state uml2withid_state) {
        this.uml2withid_states.add(uml2withid_state);
    }
    public UML2WithID_ExceptionHandler getUml2withid_exceptionhandler() {
        return uml2withid_exceptionhandler;
    }

    public void setUml2withid_exceptionhandler(UML2WithID_ExceptionHandler uml2withid_exceptionhandler) {
        this.uml2withid_exceptionhandler = uml2withid_exceptionhandler;
    }

}