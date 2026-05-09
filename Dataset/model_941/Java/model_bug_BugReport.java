





import java.util.List;
import java.util.ArrayList;

public class model_bug_BugReport extends task_WorkItem, task_Checkable {

    private String severity;
    private boolean done;
    private String resolutionType;
    private String resolution;



    public model_bug_BugReport(
        String severity,        boolean done,        String resolutionType,        String resolution    ) {
        super(
        );
        this.severity = severity;
        this.done = done;
        this.resolutionType = resolutionType;
        this.resolution = resolution;
    }


    public String getSeverity() {
        return severity;
    }

    public void setSeverity(String severity) {
        this.severity = severity;
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
    public String getResolution() {
        return resolution;
    }

    public void setResolution(String resolution) {
        this.resolution = resolution;
    }


}