





import java.util.List;
import java.util.ArrayList;

public class requirementEngineeringLanguage_Interaction extends When {

    private String target;
    private String action;



    public requirementEngineeringLanguage_Interaction(
        String target,        String action    ) {
        super(
        );
        this.target = target;
        this.action = action;
    }


    public String getTarget() {
        return target;
    }

    public void setTarget(String target) {
        this.target = target;
    }
    public String getAction() {
        return action;
    }

    public void setAction(String action) {
        this.action = action;
    }


}