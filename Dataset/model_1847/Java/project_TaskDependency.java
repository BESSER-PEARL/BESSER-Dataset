





import java.util.List;
import java.util.ArrayList;

public class project_TaskDependency extends Precedes, Depends {

    private String policy;





    private project_Task project_task;




    private project_GapDuration project_gapduration;




    private project_GapLength project_gaplength;


    public project_TaskDependency(
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

    public project_Task getProject_task() {
        return project_task;
    }

    public void setProject_task(project_Task project_task) {
        this.project_task = project_task;
    }
    public project_GapDuration getProject_gapduration() {
        return project_gapduration;
    }

    public void setProject_gapduration(project_GapDuration project_gapduration) {
        this.project_gapduration = project_gapduration;
    }
    public project_GapLength getProject_gaplength() {
        return project_gaplength;
    }

    public void setProject_gaplength(project_GapLength project_gaplength) {
        this.project_gaplength = project_gaplength;
    }

}