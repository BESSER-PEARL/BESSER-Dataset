





import java.util.List;
import java.util.ArrayList;

public class UML2_BehavioredClassifier extends Classifier {






    private List<UML2_Trigger> uml2_triggers;




    private UML2_Behavior uml2_behavior;




    private List<UML2_Behavior> uml2_behaviors;




    private UML2_Behavior uml2_behavior;


    public UML2_BehavioredClassifier(
    ) {
        super(
        );
        this.uml2_triggers = new ArrayList<>();
        this.uml2_behaviors = new ArrayList<>();
    }

    public UML2_BehavioredClassifier(
        ArrayList<UML2_Trigger> uml2_triggers,        ArrayList<UML2_Behavior> uml2_behaviors    ) {
        this.uml2_triggers = uml2_triggers;
        this.uml2_behaviors = uml2_behaviors;
    }


    public List<UML2_Trigger> getUml2_triggers() {
        return uml2_triggers;
    }

    public void addUml2_trigger(Uml2_trigger uml2_trigger) {
        this.uml2_triggers.add(uml2_trigger);
    }
    public UML2_Behavior getUml2_behavior() {
        return uml2_behavior;
    }

    public void setUml2_behavior(UML2_Behavior uml2_behavior) {
        this.uml2_behavior = uml2_behavior;
    }
    public List<UML2_Behavior> getUml2_behaviors() {
        return uml2_behaviors;
    }

    public void addUml2_behavior(Uml2_behavior uml2_behavior) {
        this.uml2_behaviors.add(uml2_behavior);
    }
    public UML2_Behavior getUml2_behavior() {
        return uml2_behavior;
    }

    public void setUml2_behavior(UML2_Behavior uml2_behavior) {
        this.uml2_behavior = uml2_behavior;
    }

}