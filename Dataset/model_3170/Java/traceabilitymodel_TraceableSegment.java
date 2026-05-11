





import java.util.List;
import java.util.ArrayList;

public class traceabilitymodel_TraceableSegment  {

    private String endPos;
    private String startColumn;
    private String startLine;
    private String startPos;
    private String endLine;
    private String endColumn;





    private traceabilitymodel_Trace traceabilitymodel_trace;


    public traceabilitymodel_TraceableSegment(
        String endPos,        String startColumn,        String startLine,        String startPos,        String endLine,        String endColumn    ) {
        this.endPos = endPos;
        this.startColumn = startColumn;
        this.startLine = startLine;
        this.startPos = startPos;
        this.endLine = endLine;
        this.endColumn = endColumn;
    }


    public String getEndpos() {
        return endPos;
    }

    public void setEndpos(String endPos) {
        this.endPos = endPos;
    }
    public String getStartcolumn() {
        return startColumn;
    }

    public void setStartcolumn(String startColumn) {
        this.startColumn = startColumn;
    }
    public String getStartline() {
        return startLine;
    }

    public void setStartline(String startLine) {
        this.startLine = startLine;
    }
    public String getStartpos() {
        return startPos;
    }

    public void setStartpos(String startPos) {
        this.startPos = startPos;
    }
    public String getEndline() {
        return endLine;
    }

    public void setEndline(String endLine) {
        this.endLine = endLine;
    }
    public String getEndcolumn() {
        return endColumn;
    }

    public void setEndcolumn(String endColumn) {
        this.endColumn = endColumn;
    }

    public traceabilitymodel_Trace getTraceabilitymodel_trace() {
        return traceabilitymodel_trace;
    }

    public void setTraceabilitymodel_trace(traceabilitymodel_Trace traceabilitymodel_trace) {
        this.traceabilitymodel_trace = traceabilitymodel_trace;
    }

}