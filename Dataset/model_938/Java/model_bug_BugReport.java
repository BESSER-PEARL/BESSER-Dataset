





import java.util.List;
import java.util.ArrayList;

public class model_bug_BugReport extends task_Checkable, task_WorkItem {

    private String resolutionType;
    private String resolution;
    private String Status;
    private String severity;



    public model_bug_BugReport(
        String resolutionType,        String resolution,        String Status,        String severity    ) {
        super(
        );
        this.resolutionType = resolutionType;
        this.resolution = resolution;
        this.Status = Status;
        this.severity = severity;
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
    public String getStatus() {
        return Status;
    }

    public void setStatus(String Status) {
        this.Status = Status;
    }
    public String getSeverity() {
        return severity;
    }

    public void setSeverity(String severity) {
        this.severity = severity;
    }


}