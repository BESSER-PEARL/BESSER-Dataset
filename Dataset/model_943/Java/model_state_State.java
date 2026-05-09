





import java.util.List;
import java.util.ArrayList;

public class model_state_State extends StateNode {

    private String entryConditions;
    private String activities;
    private String exitConditions;



    public model_state_State(
        String entryConditions,        String activities,        String exitConditions    ) {
        super(
        );
        this.entryConditions = entryConditions;
        this.activities = activities;
        this.exitConditions = exitConditions;
    }


    public String getEntryconditions() {
        return entryConditions;
    }

    public void setEntryconditions(String entryConditions) {
        this.entryConditions = entryConditions;
    }
    public String getActivities() {
        return activities;
    }

    public void setActivities(String activities) {
        this.activities = activities;
    }
    public String getExitconditions() {
        return exitConditions;
    }

    public void setExitconditions(String exitConditions) {
        this.exitConditions = exitConditions;
    }


}