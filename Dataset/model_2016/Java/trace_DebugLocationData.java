





import java.util.List;
import java.util.ArrayList;

public class trace_DebugLocationData  {

    private String label;
    private int lineNumber;
    private int length;
    private int endLineNumber;
    private String path;
    private int offset;
    private int endOffset;





    private trace_DebugTraceRegion trace_debugtraceregion;


    public trace_DebugLocationData(
        String label,        int lineNumber,        int length,        int endLineNumber,        String path,        int offset,        int endOffset    ) {
        this.label = label;
        this.lineNumber = lineNumber;
        this.length = length;
        this.endLineNumber = endLineNumber;
        this.path = path;
        this.offset = offset;
        this.endOffset = endOffset;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public int getLinenumber() {
        return lineNumber;
    }

    public void setLinenumber(int lineNumber) {
        this.lineNumber = lineNumber;
    }
    public int getLength() {
        return length;
    }

    public void setLength(int length) {
        this.length = length;
    }
    public int getEndlinenumber() {
        return endLineNumber;
    }

    public void setEndlinenumber(int endLineNumber) {
        this.endLineNumber = endLineNumber;
    }
    public String getPath() {
        return path;
    }

    public void setPath(String path) {
        this.path = path;
    }
    public int getOffset() {
        return offset;
    }

    public void setOffset(int offset) {
        this.offset = offset;
    }
    public int getEndoffset() {
        return endOffset;
    }

    public void setEndoffset(int endOffset) {
        this.endOffset = endOffset;
    }

    public trace_DebugTraceRegion getTrace_debugtraceregion() {
        return trace_debugtraceregion;
    }

    public void setTrace_debugtraceregion(trace_DebugTraceRegion trace_debugtraceregion) {
        this.trace_debugtraceregion = trace_debugtraceregion;
    }

}