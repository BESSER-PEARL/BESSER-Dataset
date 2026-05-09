





import java.util.List;
import java.util.ArrayList;

public class graph_GIssue  {

    private String message;
    private String severity;





    private graph_GIssueMarker graph_gissuemarker;


    public graph_GIssue(
        String message,        String severity    ) {
        this.message = message;
        this.severity = severity;
    }


    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
    public String getSeverity() {
        return severity;
    }

    public void setSeverity(String severity) {
        this.severity = severity;
    }

    public graph_GIssueMarker getGraph_gissuemarker() {
        return graph_gissuemarker;
    }

    public void setGraph_gissuemarker(graph_GIssueMarker graph_gissuemarker) {
        this.graph_gissuemarker = graph_gissuemarker;
    }

}