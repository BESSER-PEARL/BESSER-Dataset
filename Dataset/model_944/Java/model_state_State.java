





import java.util.List;
import java.util.ArrayList;

public class model_state_State extends StateNode {

    private String entryConditions;
    private String exitConditions;
    private String activities;



    public model_state_State(
        String entryConditions,        String exitConditions,        String activities    ) {
        super(
        );
        this.entryConditions = entryConditions;
        this.exitConditions = exitConditions;
        this.activities = activities;
    }


    public String getEntryconditions() {
        return entryConditions;
    }

    public void setEntryconditions(String entryConditions) {
        this.entryConditions = entryConditions;
    }
    public String getExitconditions() {
        return exitConditions;
    }

    public void setExitconditions(String exitConditions) {
        this.exitConditions = exitConditions;
    }
    public String getActivities() {
        return activities;
    }

    public void setActivities(String activities) {
        this.activities = activities;
    }


}