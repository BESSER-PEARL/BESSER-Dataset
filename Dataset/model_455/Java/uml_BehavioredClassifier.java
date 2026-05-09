





import java.util.List;
import java.util.ArrayList;

public class uml_BehavioredClassifier extends Classifier {






    private List<uml_Trigger> uml_triggers;


    public uml_BehavioredClassifier(
    ) {
        super(
        );
        this.uml_triggers = new ArrayList<>();
    }

    public uml_BehavioredClassifier(
        ArrayList<uml_Trigger> uml_triggers    ) {
        this.uml_triggers = uml_triggers;
    }


    public List<uml_Trigger> getUml_triggers() {
        return uml_triggers;
    }

    public void addUml_trigger(Uml_trigger uml_trigger) {
        this.uml_triggers.add(uml_trigger);
    }

}