





import java.util.List;
import java.util.ArrayList;

public class guigraph_ConditionActionTransition extends Transition {

    private String applicationConditionText;
    private String actionsText;





    private Predicate predicate;


    public guigraph_ConditionActionTransition(
        String applicationConditionText,        String actionsText    ) {
        super(
        );
        this.applicationConditionText = applicationConditionText;
        this.actionsText = actionsText;
    }


    public String getApplicationconditiontext() {
        return applicationConditionText;
    }

    public void setApplicationconditiontext(String applicationConditionText) {
        this.applicationConditionText = applicationConditionText;
    }
    public String getActionstext() {
        return actionsText;
    }

    public void setActionstext(String actionsText) {
        this.actionsText = actionsText;
    }

    public Predicate getPredicate() {
        return predicate;
    }

    public void setPredicate(Predicate predicate) {
        this.predicate = predicate;
    }

}