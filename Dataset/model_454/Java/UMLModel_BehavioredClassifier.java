





import java.util.List;
import java.util.ArrayList;

public class UMLModel_BehavioredClassifier extends Classifier {

    private String classifierBehavior;





    private List<UMLModel_Trigger> umlmodel_triggers;




    private List<UMLModel_Behavior> umlmodel_behaviors;


    public UMLModel_BehavioredClassifier(
        String classifierBehavior    ) {
        super(
        );
        this.classifierBehavior = classifierBehavior;
        this.umlmodel_triggers = new ArrayList<>();
        this.umlmodel_behaviors = new ArrayList<>();
    }

    public UMLModel_BehavioredClassifier(
        String classifierBehavior        ArrayList<UMLModel_Trigger> umlmodel_triggers,        ArrayList<UMLModel_Behavior> umlmodel_behaviors    ) {
        this.classifierBehavior = classifierBehavior;
        this.umlmodel_triggers = umlmodel_triggers;
        this.umlmodel_behaviors = umlmodel_behaviors;
    }

    public String getClassifierbehavior() {
        return classifierBehavior;
    }

    public void setClassifierbehavior(String classifierBehavior) {
        this.classifierBehavior = classifierBehavior;
    }

    public List<UMLModel_Trigger> getUmlmodel_triggers() {
        return umlmodel_triggers;
    }

    public void addUmlmodel_trigger(Umlmodel_trigger umlmodel_trigger) {
        this.umlmodel_triggers.add(umlmodel_trigger);
    }
    public List<UMLModel_Behavior> getUmlmodel_behaviors() {
        return umlmodel_behaviors;
    }

    public void addUmlmodel_behavior(Umlmodel_behavior umlmodel_behavior) {
        this.umlmodel_behaviors.add(umlmodel_behavior);
    }

}