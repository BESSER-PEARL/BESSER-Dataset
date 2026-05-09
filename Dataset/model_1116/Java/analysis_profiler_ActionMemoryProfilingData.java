





import java.util.List;
import java.util.ArrayList;

public class analysis_profiler_ActionMemoryProfilingData  {

    private String actor;
    private String action;



    public analysis_profiler_ActionMemoryProfilingData(
        String actor,        String action    ) {
        this.actor = actor;
        this.action = action;
    }


    public String getActor() {
        return actor;
    }

    public void setActor(String actor) {
        this.actor = actor;
    }
    public String getAction() {
        return action;
    }

    public void setAction(String action) {
        this.action = action;
    }


}