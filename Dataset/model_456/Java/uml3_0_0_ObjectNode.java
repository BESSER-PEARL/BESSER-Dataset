





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_ObjectNode extends ActivityNode, TypedElement {

    private String isControlType;
    private String ordering;





    private uml3_0_0_ExceptionHandler uml3_0_0_exceptionhandler;




    private uml3_0_0_ValueSpecification uml3_0_0_valuespecification;




    private List<uml3_0_0_State> uml3_0_0_states;


    public uml3_0_0_ObjectNode(
        String isControlType,        String ordering    ) {
        super(
        );
        this.isControlType = isControlType;
        this.ordering = ordering;
        this.uml3_0_0_states = new ArrayList<>();
    }

    public uml3_0_0_ObjectNode(
        String isControlType,        String ordering        ArrayList<uml3_0_0_State> uml3_0_0_states    ) {
        this.isControlType = isControlType;
        this.ordering = ordering;
        this.uml3_0_0_states = uml3_0_0_states;
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

    public uml3_0_0_ExceptionHandler getUml3_0_0_exceptionhandler() {
        return uml3_0_0_exceptionhandler;
    }

    public void setUml3_0_0_exceptionhandler(uml3_0_0_ExceptionHandler uml3_0_0_exceptionhandler) {
        this.uml3_0_0_exceptionhandler = uml3_0_0_exceptionhandler;
    }
    public uml3_0_0_ValueSpecification getUml3_0_0_valuespecification() {
        return uml3_0_0_valuespecification;
    }

    public void setUml3_0_0_valuespecification(uml3_0_0_ValueSpecification uml3_0_0_valuespecification) {
        this.uml3_0_0_valuespecification = uml3_0_0_valuespecification;
    }
    public List<uml3_0_0_State> getUml3_0_0_states() {
        return uml3_0_0_states;
    }

    public void addUml3_0_0_state(Uml3_0_0_state uml3_0_0_state) {
        this.uml3_0_0_states.add(uml3_0_0_state);
    }

}