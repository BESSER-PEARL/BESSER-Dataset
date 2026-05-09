





import java.util.List;
import java.util.ArrayList;

public class model_state_State extends StateNode {

    private String exitConditions;
    private String activities;
    private String entryConditions;



    public model_state_State(
        String exitConditions,        String activities,        String entryConditions    ) {
        super(
        );
        this.exitConditions = exitConditions;
        this.activities = activities;
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
    public String getEntryconditions() {
        return entryConditions;
    }

    public void setEntryconditions(String entryConditions) {
        this.entryConditions = entryConditions;
    }


}