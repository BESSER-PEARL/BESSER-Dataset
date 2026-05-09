





import java.util.List;
import java.util.ArrayList;

public class analysis_postprocessing_StatisticalActorPartition  {

    private String schedulingPolicy;
    private String actors;
    private float occupancy;



    public analysis_postprocessing_StatisticalActorPartition(
        String schedulingPolicy,        String actors,        float occupancy    ) {
        this.schedulingPolicy = schedulingPolicy;
        this.actors = actors;
        this.occupancy = occupancy;
    }


    public String getSchedulingpolicy() {
        return schedulingPolicy;
    }

    public void setSchedulingpolicy(String schedulingPolicy) {
        this.schedulingPolicy = schedulingPolicy;
    }
    public String getActors() {
        return actors;
    }

    public void setActors(String actors) {
        this.actors = actors;
    }
    public float getOccupancy() {
        return occupancy;
    }

    public void setOccupancy(float occupancy) {
        this.occupancy = occupancy;
    }


}