





import java.util.List;
import java.util.ArrayList;

public class workflow_Activity  {

    private boolean started;
    private boolean finished;





    private workflow_Case workflow_case;


    public workflow_Activity(
        boolean started,        boolean finished    ) {
        this.started = started;
        this.finished = finished;
    }


    public boolean getStarted() {
        return started;
    }

    public void setStarted(boolean started) {
        this.started = started;
    }
    public boolean getFinished() {
        return finished;
    }

    public void setFinished(boolean finished) {
        this.finished = finished;
    }

    public workflow_Case getWorkflow_case() {
        return workflow_case;
    }

    public void setWorkflow_case(workflow_Case workflow_case) {
        this.workflow_case = workflow_case;
    }

}