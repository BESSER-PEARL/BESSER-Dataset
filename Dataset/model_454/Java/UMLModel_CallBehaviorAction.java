





import java.util.List;
import java.util.ArrayList;

public class UMLModel_CallBehaviorAction extends CallAction {

    private String behavior;



    public UMLModel_CallBehaviorAction(
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