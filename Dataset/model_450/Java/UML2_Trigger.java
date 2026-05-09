





import java.util.List;
import java.util.ArrayList;

public class UML2_Trigger extends NamedElement {






    private UML2_BehavioredClassifier uml2_behavioredclassifier;




    private UML2_Transition uml2_transition;




    private List<UML2_Port> uml2_ports;




    private UML2_State uml2_state;


    public UML2_Trigger(
    ) {
        super(
        );
        this.uml2_ports = new ArrayList<>();
    }

    public UML2_Trigger(
        ArrayList<UML2_Port> uml2_ports    ) {
        this.uml2_ports = uml2_ports;
    }


    public UML2_BehavioredClassifier getUml2_behavioredclassifier() {
        return uml2_behavioredclassifier;
    }

    public void setUml2_behavioredclassifier(UML2_BehavioredClassifier uml2_behavioredclassifier) {
        this.uml2_behavioredclassifier = uml2_behavioredclassifier;
    }
    public UML2_Transition getUml2_transition() {
        return uml2_transition;
    }

    public void setUml2_transition(UML2_Transition uml2_transition) {
        this.uml2_transition = uml2_transition;
    }
    public List<UML2_Port> getUml2_ports() {
        return uml2_ports;
    }

    public void addUml2_port(Uml2_port uml2_port) {
        this.uml2_ports.add(uml2_port);
    }
    public UML2_State getUml2_state() {
        return uml2_state;
    }

    public void setUml2_state(UML2_State uml2_state) {
        this.uml2_state = uml2_state;
    }

}