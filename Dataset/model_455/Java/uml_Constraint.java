





import java.util.List;
import java.util.ArrayList;

public class uml_Constraint extends PackageableElement {






    private uml_State uml_state;




    private uml_Extend uml_extend;




    private uml_Transition uml_transition;




    private List<uml_Element> uml_elements;


    public uml_Constraint(
    ) {
        super(
        );
        this.uml_elements = new ArrayList<>();
    }

    public uml_Constraint(
        ArrayList<uml_Element> uml_elements    ) {
        this.uml_elements = uml_elements;
    }


    public uml_State getUml_state() {
        return uml_state;
    }

    public void setUml_state(uml_State uml_state) {
        this.uml_state = uml_state;
    }
    public uml_Extend getUml_extend() {
        return uml_extend;
    }

    public void setUml_extend(uml_Extend uml_extend) {
        this.uml_extend = uml_extend;
    }
    public uml_Transition getUml_transition() {
        return uml_transition;
    }

    public void setUml_transition(uml_Transition uml_transition) {
        this.uml_transition = uml_transition;
    }
    public List<uml_Element> getUml_elements() {
        return uml_elements;
    }

    public void addUml_element(Uml_element uml_element) {
        this.uml_elements.add(uml_element);
    }

}