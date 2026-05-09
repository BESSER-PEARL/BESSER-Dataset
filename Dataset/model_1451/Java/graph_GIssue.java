





import java.util.List;
import java.util.ArrayList;

public class graph_GIssue  {

    private String severity;
    private String message;



    public graph_GIssue(
        String severity,        String message    ) {
        this.severity = severity;
        this.message = message;
    }


    public String getSeverity() {
        return severity;
    }

    public void setSeverity(String severity) {
        this.severity = severity;
    }
    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }


}