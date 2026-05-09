





import java.util.List;
import java.util.ArrayList;

public class model_bug_BugReport extends task_WorkItem, task_Checkable {

    private boolean done;
    private String severity;
    private String resolution;
    private String resolutionType;



    public model_bug_BugReport(
        boolean done,        String severity,        String resolution,        String resolutionType    ) {
        super(
        );
        this.done = done;
        this.severity = severity;
        this.resolution = resolution;
        this.resolutionType = resolutionType;
    }


    public boolean getDone() {
        return done;
    }

    public void setDone(boolean done) {
        this.done = done;
    }
    public String getSeverity() {
        return severity;
    }

    public void setSeverity(String severity) {
        this.severity = severity;
    }
    public String getResolution() {
        return resolution;
    }

    public void setResolution(String resolution) {
        this.resolution = resolution;
    }
    public String getResolutiontype() {
        return resolutionType;
    }

    public void setResolutiontype(String resolutionType) {
        this.resolutionType = resolutionType;
    }


}