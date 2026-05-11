





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_BehavioredClassifier extends Element {






    private UML2WithID_Behavior uml2withid_behavior;




    private List<UML2WithID_Behavior> uml2withid_behaviors;


    public UML2WithID_BehavioredClassifier(
    ) {
        super(
        );
        this.uml2withid_behaviors = new ArrayList<>();
    }

    public UML2WithID_BehavioredClassifier(
        ArrayList<UML2WithID_Behavior> uml2withid_behaviors    ) {
        this.uml2withid_behaviors = uml2withid_behaviors;
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