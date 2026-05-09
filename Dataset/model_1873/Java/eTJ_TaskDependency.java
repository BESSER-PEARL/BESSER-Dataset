





import java.util.List;
import java.util.ArrayList;

public class eTJ_TaskDependency extends Precedes {

    private String policy;





    private eTJ_Task etj_task;


    public eTJ_TaskDependency(
        String policy    ) {
        super(
        );
        this.policy = policy;
    }


    public String getPolicy() {
        return policy;
    }

    public void setPolicy(String policy) {
        this.policy = policy;
    }

    public eTJ_Task getEtj_task() {
        return etj_task;
    }

    public void setEtj_task(eTJ_Task etj_task) {
        this.etj_task = etj_task;
    }

}