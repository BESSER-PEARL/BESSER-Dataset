





import java.util.List;
import java.util.ArrayList;

public class MARTE_GRM_Scheduler extends Resource {

    private String schedPolicy;
    private String otherSchedPolicy;
    private String isPreemptible;
    private String schedule;



    public MARTE_GRM_Scheduler(
        String schedPolicy,        String otherSchedPolicy,        String isPreemptible,        String schedule    ) {
        super(
        );
        this.schedPolicy = schedPolicy;
        this.otherSchedPolicy = otherSchedPolicy;
        this.isPreemptible = isPreemptible;
        this.schedule = schedule;
    }


    public String getSchedpolicy() {
        return schedPolicy;
    }

    public void setSchedpolicy(String schedPolicy) {
        this.schedPolicy = schedPolicy;
    }
    public String getOtherschedpolicy() {
        return otherSchedPolicy;
    }

    public void setOtherschedpolicy(String otherSchedPolicy) {
        this.otherSchedPolicy = otherSchedPolicy;
    }
    public String getIspreemptible() {
        return isPreemptible;
    }

    public void setIspreemptible(String isPreemptible) {
        this.isPreemptible = isPreemptible;
    }
    public String getSchedule() {
        return schedule;
    }

    public void setSchedule(String schedule) {
        this.schedule = schedule;
    }


}