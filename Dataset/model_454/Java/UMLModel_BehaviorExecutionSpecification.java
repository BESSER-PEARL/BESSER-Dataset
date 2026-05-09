





import java.util.List;
import java.util.ArrayList;

public class UMLModel_BehaviorExecutionSpecification extends ExecutionSpecification {

    private String behavior;



    public UMLModel_BehaviorExecutionSpecification(
        String behavior    ) {
        super(
        );
        this.behavior = behavior;
    }


    public String getBehavior() {
        return behavior;
    }

    public void setBehavior(String behavior) {
        this.behavior = behavior;
    }


}