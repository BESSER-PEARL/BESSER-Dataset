





import java.util.List;
import java.util.ArrayList;

public class MARTE_SW_Concurrency_SwSchedulableResource extends SW_Concurrency_SwConcurrentResource, GRM_SchedulableResource {

    private String isPreemptable;
    private String isStaticSchedulingFeature;



    public MARTE_SW_Concurrency_SwSchedulableResource(
        String isPreemptable,        String isStaticSchedulingFeature    ) {
        super(
        );
        this.isPreemptable = isPreemptable;
        this.isStaticSchedulingFeature = isStaticSchedulingFeature;
    }


    public String getIspreemptable() {
        return isPreemptable;
    }

    public void setIspreemptable(String isPreemptable) {
        this.isPreemptable = isPreemptable;
    }
    public String getIsstaticschedulingfeature() {
        return isStaticSchedulingFeature;
    }

    public void setIsstaticschedulingfeature(String isStaticSchedulingFeature) {
        this.isStaticSchedulingFeature = isStaticSchedulingFeature;
    }


}