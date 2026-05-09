





import java.util.List;
import java.util.ArrayList;

public class analysis_scheduling_ActorFire extends ActorSelectionSchedule {

    private String dependencyPartitions;
    private String Actor;
    private String partition;
    private int Times;



    public analysis_scheduling_ActorFire(
        String dependencyPartitions,        String Actor,        String partition,        int Times    ) {
        super(
        );
        this.dependencyPartitions = dependencyPartitions;
        this.Actor = Actor;
        this.partition = partition;
        this.Times = Times;
    }


    public String getDependencypartitions() {
        return dependencyPartitions;
    }

    public void setDependencypartitions(String dependencyPartitions) {
        this.dependencyPartitions = dependencyPartitions;
    }
    public String getActor() {
        return Actor;
    }

    public void setActor(String Actor) {
        this.Actor = Actor;
    }
    public String getPartition() {
        return partition;
    }

    public void setPartition(String partition) {
        this.partition = partition;
    }
    public int getTimes() {
        return Times;
    }

    public void setTimes(int Times) {
        this.Times = Times;
    }


}