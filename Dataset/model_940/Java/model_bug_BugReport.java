





import java.util.List;
import java.util.ArrayList;

public class model_bug_BugReport extends task_WorkItem, task_Checkable {

    private String Status;
    private String resolution;
    private String resolutionType;
    private String severity;



    public model_bug_BugReport(
        String Status,        String resolution,        String resolutionType,        String severity    ) {
        super(
        );
        this.Status = Status;
        this.resolution = resolution;
        this.resolutionType = resolutionType;
        this.severity = severity;
    }


    public String getStatus() {
        return Status;
    }

    public void setStatus(String Status) {
        this.Status = Status;
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
    public String getSeverity() {
        return severity;
    }

    public void setSeverity(String severity) {
        this.severity = severity;
    }


}