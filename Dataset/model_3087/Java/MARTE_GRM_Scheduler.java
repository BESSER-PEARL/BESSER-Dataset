





import java.util.List;
import java.util.ArrayList;

public class MARTE_GRM_Scheduler extends Resource {

    private String isPreemptible;
    private String otherSchedPolicy;
    private String schedPolicy;



    public MARTE_GRM_Scheduler(
        String isPreemptible,        String otherSchedPolicy,        String schedPolicy    ) {
        super(
        );
        this.isPreemptible = isPreemptible;
        this.otherSchedPolicy = otherSchedPolicy;
        this.schedPolicy = schedPolicy;
    }


    public String getIspreemptible() {
        return isPreemptible;
    }

    public void setIspreemptible(String isPreemptible) {
        this.isPreemptible = isPreemptible;
    }
    public String getOtherschedpolicy() {
        return otherSchedPolicy;
    }

    public void setOtherschedpolicy(String otherSchedPolicy) {
        this.otherSchedPolicy = otherSchedPolicy;
    }
    public String getSchedpolicy() {
        return schedPolicy;
    }

    public void setSchedpolicy(String schedPolicy) {
        this.schedPolicy = schedPolicy;
    }


}