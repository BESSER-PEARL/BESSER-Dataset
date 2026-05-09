





import java.util.List;
import java.util.ArrayList;

public class fuml_BasicBehaviors_Behavior extends Class {

    private boolean reentrant;





    private BasicBehaviors_BehavioredClassifier basicbehaviors_behavioredclassifier;


    public fuml_BasicBehaviors_Behavior(
        boolean reentrant    ) {
        super(
        );
        this.reentrant = reentrant;
    }


    public boolean getReentrant() {
        return reentrant;
    }

    public void setReentrant(boolean reentrant) {
        this.reentrant = reentrant;
    }

    public BasicBehaviors_BehavioredClassifier getBasicbehaviors_behavioredclassifier() {
        return basicbehaviors_behavioredclassifier;
    }

    public void setBasicbehaviors_behavioredclassifier(BasicBehaviors_BehavioredClassifier basicbehaviors_behavioredclassifier) {
        this.basicbehaviors_behavioredclassifier = basicbehaviors_behavioredclassifier;
    }

}