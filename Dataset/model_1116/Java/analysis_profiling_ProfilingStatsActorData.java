





import java.util.List;
import java.util.ArrayList;

public class analysis_profiling_ProfilingStatsActorData  {

    private float schedulerWeight;
    private String actorName;
    private float actionsWeightPercent;
    private float actionsWeight;
    private float schedulerWeightPercent;



    public analysis_profiling_ProfilingStatsActorData(
        float schedulerWeight,        String actorName,        float actionsWeightPercent,        float actionsWeight,        float schedulerWeightPercent    ) {
        this.schedulerWeight = schedulerWeight;
        this.actorName = actorName;
        this.actionsWeightPercent = actionsWeightPercent;
        this.actionsWeight = actionsWeight;
        this.schedulerWeightPercent = schedulerWeightPercent;
    }


    public float getSchedulerweight() {
        return schedulerWeight;
    }

    public void setSchedulerweight(float schedulerWeight) {
        this.schedulerWeight = schedulerWeight;
    }
    public String getActorname() {
        return actorName;
    }

    public void setActorname(String actorName) {
        this.actorName = actorName;
    }
    public float getActionsweightpercent() {
        return actionsWeightPercent;
    }

    public void setActionsweightpercent(float actionsWeightPercent) {
        this.actionsWeightPercent = actionsWeightPercent;
    }
    public float getActionsweight() {
        return actionsWeight;
    }

    public void setActionsweight(float actionsWeight) {
        this.actionsWeight = actionsWeight;
    }
    public float getSchedulerweightpercent() {
        return schedulerWeightPercent;
    }

    public void setSchedulerweightpercent(float schedulerWeightPercent) {
        this.schedulerWeightPercent = schedulerWeightPercent;
    }


}