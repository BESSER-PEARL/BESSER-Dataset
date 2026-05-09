





import java.util.List;
import java.util.ArrayList;

public class UML2_ObjectNode extends TypedElement, ActivityNode {

    private String ordering;





    private UML2_Behavior uml2_behavior;




    private List<UML2_State> uml2_states;


    public UML2_ObjectNode(
        String ordering    ) {
        super(
        );
        this.ordering = ordering;
        this.uml2_states = new ArrayList<>();
    }

    public UML2_ObjectNode(
        String ordering        ArrayList<UML2_State> uml2_states    ) {
        this.ordering = ordering;
        this.uml2_states = uml2_states;
    }

    public String getOrdering() {
        return ordering;
    }

    public void setOrdering(String ordering) {
        this.ordering = ordering;
    }

    public UML2_Behavior getUml2_behavior() {
        return uml2_behavior;
    }

    public void setUml2_behavior(UML2_Behavior uml2_behavior) {
        this.uml2_behavior = uml2_behavior;
    }
    public List<UML2_State> getUml2_states() {
        return uml2_states;
    }

    public void addUml2_state(Uml2_state uml2_state) {
        this.uml2_states.add(uml2_state);
    }

}