





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_BehavioredClassifier extends Classifier {






    private List<UML2WithID_StateMachine> uml2withid_statemachines;




    private UML2WithID_Behavior uml2withid_behavior;




    private List<UML2WithID_Implementation> uml2withid_implementations;




    private UML2WithID_Implementation uml2withid_implementation;




    private UML2WithID_StateMachine uml2withid_statemachine;




    private List<UML2WithID_Trigger> uml2withid_triggers;




    private UML2WithID_Behavior uml2withid_behavior;




    private List<UML2WithID_Behavior> uml2withid_behaviors;


    public UML2WithID_BehavioredClassifier(
    ) {
        super(
        );
        this.uml2withid_statemachines = new ArrayList<>();
        this.uml2withid_implementations = new ArrayList<>();
        this.uml2withid_triggers = new ArrayList<>();
        this.uml2withid_behaviors = new ArrayList<>();
    }

    public UML2WithID_BehavioredClassifier(
        ArrayList<UML2WithID_StateMachine> uml2withid_statemachines,        ArrayList<UML2WithID_Implementation> uml2withid_implementations,        ArrayList<UML2WithID_Trigger> uml2withid_triggers,        ArrayList<UML2WithID_Behavior> uml2withid_behaviors    ) {
        this.uml2withid_statemachines = uml2withid_statemachines;
        this.uml2withid_implementations = uml2withid_implementations;
        this.uml2withid_triggers = uml2withid_triggers;
        this.uml2withid_behaviors = uml2withid_behaviors;
    }


    public List<UML2WithID_StateMachine> getUml2withid_statemachines() {
        return uml2withid_statemachines;
    }

    public void addUml2withid_statemachine(Uml2withid_statemachine uml2withid_statemachine) {
        this.uml2withid_statemachines.add(uml2withid_statemachine);
    }
    public UML2WithID_Behavior getUml2withid_behavior() {
        return uml2withid_behavior;
    }

    public void setUml2withid_behavior(UML2WithID_Behavior uml2withid_behavior) {
        this.uml2withid_behavior = uml2withid_behavior;
    }
    public List<UML2WithID_Implementation> getUml2withid_implementations() {
        return uml2withid_implementations;
    }

    public void addUml2withid_implementation(Uml2withid_implementation uml2withid_implementation) {
        this.uml2withid_implementations.add(uml2withid_implementation);
    }
    public UML2WithID_Implementation getUml2withid_implementation() {
        return uml2withid_implementation;
    }

    public void setUml2withid_implementation(UML2WithID_Implementation uml2withid_implementation) {
        this.uml2withid_implementation = uml2withid_implementation;
    }
    public UML2WithID_StateMachine getUml2withid_statemachine() {
        return uml2withid_statemachine;
    }

    public void setUml2withid_statemachine(UML2WithID_StateMachine uml2withid_statemachine) {
        this.uml2withid_statemachine = uml2withid_statemachine;
    }
    public List<UML2WithID_Trigger> getUml2withid_triggers() {
        return uml2withid_triggers;
    }

    public void addUml2withid_trigger(Uml2withid_trigger uml2withid_trigger) {
        this.uml2withid_triggers.add(uml2withid_trigger);
    }
    public UML2WithID_Behavior getUml2withid_behavior() {
        return uml2withid_behavior;
    }

    public void setUml2withid_behavior(UML2WithID_Behavior uml2withid_behavior) {
        this.uml2withid_behavior = uml2withid_behavior;
    }
    public List<UML2WithID_Behavior> getUml2withid_behaviors() {
        return uml2withid_behaviors;
    }

    public void addUml2withid_behavior(Uml2withid_behavior uml2withid_behavior) {
        this.uml2withid_behaviors.add(uml2withid_behavior);
    }

}