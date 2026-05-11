





import java.util.List;
import java.util.ArrayList;

public class guigraph_ConditionActionTransition extends Transition {

    private String actionsText;
    private String applicationConditionText;



    public guigraph_ConditionActionTransition(
        String actionsText,        String applicationConditionText    ) {
        super(
        );
        this.actionsText = actionsText;
        this.applicationConditionText = applicationConditionText;
    }


    public String getActionstext() {
        return actionsText;
    }

    public void setActionstext(String actionsText) {
        this.actionsText = actionsText;
    }
    public String getApplicationconditiontext() {
        return applicationConditionText;
    }

    public void setApplicationconditiontext(String applicationConditionText) {
        this.applicationConditionText = applicationConditionText;
    }


}