





import java.util.List;
import java.util.ArrayList;

public class UML2_ExecutionOccurrence extends InteractionFragment {






    private List<UML2_Behavior> uml2_behaviors;


    public UML2_ExecutionOccurrence(
    ) {
        super(
        );
        this.uml2_behaviors = new ArrayList<>();
    }

    public UML2_ExecutionOccurrence(
        ArrayList<UML2_Behavior> uml2_behaviors    ) {
        this.uml2_behaviors = uml2_behaviors;
    }


    public List<UML2_Behavior> getUml2_behaviors() {
        return uml2_behaviors;
    }

    public void addUml2_behavior(Uml2_behavior uml2_behavior) {
        this.uml2_behaviors.add(uml2_behavior);
    }

}