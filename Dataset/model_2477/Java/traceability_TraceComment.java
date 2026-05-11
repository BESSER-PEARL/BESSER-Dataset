




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class traceability_TraceComment  {

    private String comment;
    private String username;
    private String column;
    private LocalDate date;





    private traceability_EObject traceability_eobject;




    private traceability_TraceDiff traceability_tracediff;




    private traceability_Trace traceability_trace;


    public traceability_TraceComment(
        String comment,        String username,        String column,        LocalDate date    ) {
        this.comment = comment;
        this.username = username;
        this.column = column;
        this.date = date;
    }


    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public String getColumn() {
        return column;
    }

    public void setColumn(String column) {
        this.column = column;
    }
    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }

    public traceability_EObject getTraceability_eobject() {
        return traceability_eobject;
    }

    public void setTraceability_eobject(traceability_EObject traceability_eobject) {
        this.traceability_eobject = traceability_eobject;
    }
    public traceability_TraceDiff getTraceability_tracediff() {
        return traceability_tracediff;
    }

    public void setTraceability_tracediff(traceability_TraceDiff traceability_tracediff) {
        this.traceability_tracediff = traceability_tracediff;
    }
    public traceability_Trace getTraceability_trace() {
        return traceability_trace;
    }

    public void setTraceability_trace(traceability_Trace traceability_trace) {
        this.traceability_trace = traceability_trace;
    }

}