





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_BehavioredClassifier extends Classifier {






    private List<uml3_0_0_Trigger> uml3_0_0_triggers;


    public uml3_0_0_BehavioredClassifier(
    ) {
        super(
        );
        this.uml3_0_0_triggers = new ArrayList<>();
    }

    public uml3_0_0_BehavioredClassifier(
        ArrayList<uml3_0_0_Trigger> uml3_0_0_triggers    ) {
        this.uml3_0_0_triggers = uml3_0_0_triggers;
    }


    public List<uml3_0_0_Trigger> getUml3_0_0_triggers() {
        return uml3_0_0_triggers;
    }

    public void addUml3_0_0_trigger(Uml3_0_0_trigger uml3_0_0_trigger) {
        this.uml3_0_0_triggers.add(uml3_0_0_trigger);
    }

}