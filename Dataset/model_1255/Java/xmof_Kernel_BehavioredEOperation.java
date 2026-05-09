





import java.util.List;
import java.util.ArrayList;

public class xmof_Kernel_BehavioredEOperation extends EOperation {






    private List<BasicBehaviors_Behavior> basicbehaviors_behaviors;


    public xmof_Kernel_BehavioredEOperation(
    ) {
        super(
        );
        this.basicbehaviors_behaviors = new ArrayList<>();
    }

    public xmof_Kernel_BehavioredEOperation(
        ArrayList<BasicBehaviors_Behavior> basicbehaviors_behaviors    ) {
        this.basicbehaviors_behaviors = basicbehaviors_behaviors;
    }


    public List<BasicBehaviors_Behavior> getBasicbehaviors_behaviors() {
        return basicbehaviors_behaviors;
    }

    public void addBasicbehaviors_behavior(Basicbehaviors_behavior basicbehaviors_behavior) {
        this.basicbehaviors_behaviors.add(basicbehaviors_behavior);
    }

}