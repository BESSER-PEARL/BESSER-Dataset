





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_Constraint extends PackageableElement {






    private uml3_0_0_Transition uml3_0_0_transition;




    private uml3_0_0_ValueSpecification uml3_0_0_valuespecification;




    private uml3_0_0_State uml3_0_0_state;




    private List<uml3_0_0_Element> uml3_0_0_elements;


    public uml3_0_0_Constraint(
    ) {
        super(
        );
        this.uml3_0_0_elements = new ArrayList<>();
    }

    public uml3_0_0_Constraint(
        ArrayList<uml3_0_0_Element> uml3_0_0_elements    ) {
        this.uml3_0_0_elements = uml3_0_0_elements;
    }


    public uml3_0_0_Transition getUml3_0_0_transition() {
        return uml3_0_0_transition;
    }

    public void setUml3_0_0_transition(uml3_0_0_Transition uml3_0_0_transition) {
        this.uml3_0_0_transition = uml3_0_0_transition;
    }
    public uml3_0_0_ValueSpecification getUml3_0_0_valuespecification() {
        return uml3_0_0_valuespecification;
    }

    public void setUml3_0_0_valuespecification(uml3_0_0_ValueSpecification uml3_0_0_valuespecification) {
        this.uml3_0_0_valuespecification = uml3_0_0_valuespecification;
    }
    public uml3_0_0_State getUml3_0_0_state() {
        return uml3_0_0_state;
    }

    public void setUml3_0_0_state(uml3_0_0_State uml3_0_0_state) {
        this.uml3_0_0_state = uml3_0_0_state;
    }
    public List<uml3_0_0_Element> getUml3_0_0_elements() {
        return uml3_0_0_elements;
    }

    public void addUml3_0_0_element(Uml3_0_0_element uml3_0_0_element) {
        this.uml3_0_0_elements.add(uml3_0_0_element);
    }

}