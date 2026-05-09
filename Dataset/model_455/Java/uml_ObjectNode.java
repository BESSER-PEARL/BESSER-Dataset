





import java.util.List;
import java.util.ArrayList;

public class uml_ObjectNode extends TypedElement, ActivityNode {

    private String isControlType;
    private String ordering;





    private List<uml_State> uml_states;




    private uml_ValueSpecification uml_valuespecification;




    private uml_ExceptionHandler uml_exceptionhandler;


    public uml_ObjectNode(
        String isControlType,        String ordering    ) {
        super(
        );
        this.isControlType = isControlType;
        this.ordering = ordering;
        this.uml_states = new ArrayList<>();
    }

    public uml_ObjectNode(
        String isControlType,        String ordering        ArrayList<uml_State> uml_states    ) {
        this.isControlType = isControlType;
        this.ordering = ordering;
        this.uml_states = uml_states;
    }

    public String getIscontroltype() {
        return isControlType;
    }

    public void setIscontroltype(String isControlType) {
        this.isControlType = isControlType;
    }
    public String getOrdering() {
        return ordering;
    }

    public void setOrdering(String ordering) {
        this.ordering = ordering;
    }

    public List<uml_State> getUml_states() {
        return uml_states;
    }

    public void addUml_state(Uml_state uml_state) {
        this.uml_states.add(uml_state);
    }
    public uml_ValueSpecification getUml_valuespecification() {
        return uml_valuespecification;
    }

    public void setUml_valuespecification(uml_ValueSpecification uml_valuespecification) {
        this.uml_valuespecification = uml_valuespecification;
    }
    public uml_ExceptionHandler getUml_exceptionhandler() {
        return uml_exceptionhandler;
    }

    public void setUml_exceptionhandler(uml_ExceptionHandler uml_exceptionhandler) {
        this.uml_exceptionhandler = uml_exceptionhandler;
    }

}