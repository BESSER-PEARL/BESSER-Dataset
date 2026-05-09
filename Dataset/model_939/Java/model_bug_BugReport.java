





import java.util.List;
import java.util.ArrayList;

public class model_bug_BugReport extends task_Checkable, task_WorkItem {

    private String resolution;
    private boolean done;
    private String resolutionType;
    private String severity;



    public model_bug_BugReport(
        String resolution,        boolean done,        String resolutionType,        String severity    ) {
        super(
        );
        this.resolution = resolution;
        this.done = done;
        this.resolutionType = resolutionType;
        this.severity = severity;
    }


    public String getResolution() {
        return resolution;
    }

    public void setResolution(String resolution) {
        this.resolution = resolution;
    }
    public boolean getDone() {
        return done;
    }

    public void setDone(boolean done) {
        this.done = done;
    }
    public String getResolutiontype() {
        return resolutionType;
    }

    public void setResolutiontype(String resolutionType) {
        this.resolutionType = resolutionType;
    }
    public String getSeverity() {
        return severity;
    }

    public void setSeverity(String severity) {
        this.severity = severity;
    }


}