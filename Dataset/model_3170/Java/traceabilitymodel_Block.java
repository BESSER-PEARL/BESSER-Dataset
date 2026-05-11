





import java.util.List;
import java.util.ArrayList;

public class traceabilitymodel_Block  {

    private boolean protectedBlock;
    private String startLine;
    private String endLine;
    private String startPos;
    private String ID;
    private String endColumn;
    private String endPos;
    private String startColumn;





    private traceabilitymodel_File traceabilitymodel_file;




    private List<traceabilitymodel_TraceableSegment> traceabilitymodel_traceablesegments;


    public traceabilitymodel_Block(
        boolean protectedBlock,        String startLine,        String endLine,        String startPos,        String ID,        String endColumn,        String endPos,        String startColumn    ) {
        this.protectedBlock = protectedBlock;
        this.startLine = startLine;
        this.endLine = endLine;
        this.startPos = startPos;
        this.ID = ID;
        this.endColumn = endColumn;
        this.endPos = endPos;
        this.startColumn = startColumn;
        this.traceabilitymodel_traceablesegments = new ArrayList<>();
    }

    public traceabilitymodel_Block(
        boolean protectedBlock,        String startLine,        String endLine,        String startPos,        String ID,        String endColumn,        String endPos,        String startColumn        ArrayList<traceabilitymodel_TraceableSegment> traceabilitymodel_traceablesegments    ) {
        this.protectedBlock = protectedBlock;
        this.startLine = startLine;
        this.endLine = endLine;
        this.startPos = startPos;
        this.ID = ID;
        this.endColumn = endColumn;
        this.endPos = endPos;
        this.startColumn = startColumn;
        this.traceabilitymodel_traceablesegments = traceabilitymodel_traceablesegments;
    }

    public boolean getProtectedblock() {
        return protectedBlock;
    }

    public void setProtectedblock(boolean protectedBlock) {
        this.protectedBlock = protectedBlock;
    }
    public String getStartline() {
        return startLine;
    }

    public void setStartline(String startLine) {
        this.startLine = startLine;
    }
    public String getEndline() {
        return endLine;
    }

    public void setEndline(String endLine) {
        this.endLine = endLine;
    }
    public String getStartpos() {
        return startPos;
    }

    public void setStartpos(String startPos) {
        this.startPos = startPos;
    }
    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }
    public String getEndcolumn() {
        return endColumn;
    }

    public void setEndcolumn(String endColumn) {
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

    public traceabilitymodel_File getTraceabilitymodel_file() {
        return traceabilitymodel_file;
    }

    public void setTraceabilitymodel_file(traceabilitymodel_File traceabilitymodel_file) {
        this.traceabilitymodel_file = traceabilitymodel_file;
    }
    public List<traceabilitymodel_TraceableSegment> getTraceabilitymodel_traceablesegments() {
        return traceabilitymodel_traceablesegments;
    }

    public void addTraceabilitymodel_traceablesegment(Traceabilitymodel_traceablesegment traceabilitymodel_traceablesegment) {
        this.traceabilitymodel_traceablesegments.add(traceabilitymodel_traceablesegment);
    }

}