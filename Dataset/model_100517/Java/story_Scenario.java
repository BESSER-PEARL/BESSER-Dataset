





import java.util.List;
import java.util.ArrayList;

public class story_Scenario extends CatalogElement {

    private String action;
    private String outcome;
    private String context;



    public story_Scenario(
        String action,        String outcome,        String context    ) {
        super(
        );
        this.action = action;
        this.outcome = outcome;
        this.context = context;
    }


    public String getAction() {
        return action;
    }

    public void setAction(String action) {
        this.action = action;
    }
    public String getOutcome() {
        return outcome;
    }

    public void setOutcome(String outcome) {
        this.outcome = outcome;
    }
    public String getContext() {
        return context;
    }

    public void setContext(String context) {
        this.context = context;
    }


}