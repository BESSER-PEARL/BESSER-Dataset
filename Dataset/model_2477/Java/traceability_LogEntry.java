





import java.util.List;
import java.util.ArrayList;

public class traceability_LogEntry  {

    private int messageType;
    private String comment;
    private int severity;
    private String message;





    private List<traceability_TraceComment> traceability_tracecomments;




    private List<traceability_EObject> traceability_eobjects;


    public traceability_LogEntry(
        int messageType,        String comment,        int severity,        String message    ) {
        this.messageType = messageType;
        this.comment = comment;
        this.severity = severity;
        this.message = message;
        this.traceability_tracecomments = new ArrayList<>();
        this.traceability_eobjects = new ArrayList<>();
    }

    public traceability_LogEntry(
        int messageType,        String comment,        int severity,        String message        ArrayList<traceability_TraceComment> traceability_tracecomments,        ArrayList<traceability_EObject> traceability_eobjects    ) {
        this.messageType = messageType;
        this.comment = comment;
        this.severity = severity;
        this.message = message;
        this.traceability_tracecomments = traceability_tracecomments;
        this.traceability_eobjects = traceability_eobjects;
    }

    public int getMessagetype() {
        return messageType;
    }

    public void setMessagetype(int messageType) {
        this.messageType = messageType;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public int getSeverity() {
        return severity;
    }

    public void setSeverity(int severity) {
        this.severity = severity;
    }
    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }

    public List<traceability_TraceComment> getTraceability_tracecomments() {
        return traceability_tracecomments;
    }

    public void addTraceability_tracecomment(Traceability_tracecomment traceability_tracecomment) {
        this.traceability_tracecomments.add(traceability_tracecomment);
    }
    public List<traceability_EObject> getTraceability_eobjects() {
        return traceability_eobjects;
    }

    public void addTraceability_eobject(Traceability_eobject traceability_eobject) {
        this.traceability_eobjects.add(traceability_eobject);
    }

}