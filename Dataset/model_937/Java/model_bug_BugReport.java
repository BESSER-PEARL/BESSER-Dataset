





import java.util.List;
import java.util.ArrayList;

public class model_bug_BugReport extends task_Checkable, task_WorkItem {

    private String Status;
    private String resolutionType;
    private String severity;
    private String resolution;



    public model_bug_BugReport(
        String Status,        String resolutionType,        String severity,        String resolution    ) {
        super(
        );
        this.Status = Status;
        this.resolutionType = resolutionType;
        this.severity = severity;
        this.resolution = resolution;
    }


    public String getStatus() {
        return Status;
    }

    public void setStatus(String Status) {
        this.Status = Status;
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
    public String getResolution() {
        return resolution;
    }

    public void setResolution(String resolution) {
        this.resolution = resolution;
    }


}