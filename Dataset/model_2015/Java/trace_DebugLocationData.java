





import java.util.List;
import java.util.ArrayList;

public class trace_DebugLocationData  {

    private int length;
    private int offset;
    private int lineNumber;
    private String label;
    private String path;
    private int endOffset;
    private int endLineNumber;



    public trace_DebugLocationData(
        int length,        int offset,        int lineNumber,        String label,        String path,        int endOffset,        int endLineNumber    ) {
        this.length = length;
        this.offset = offset;
        this.lineNumber = lineNumber;
        this.label = label;
        this.path = path;
        this.endOffset = endOffset;
        this.endLineNumber = endLineNumber;
    }


    public int getLength() {
        return length;
    }

    public void setLength(int length) {
        this.length = length;
    }
    public int getOffset() {
        return offset;
    }

    public void setOffset(int offset) {
        this.offset = offset;
    }
    public int getLinenumber() {
        return lineNumber;
    }

    public void setLinenumber(int lineNumber) {
        this.lineNumber = lineNumber;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getPath() {
        return path;
    }

    public void setPath(String path) {
        this.path = path;
    }
    public int getEndoffset() {
        return endOffset;
    }

    public void setEndoffset(int endOffset) {
        this.endOffset = endOffset;
    }
    public int getEndlinenumber() {
        return endLineNumber;
    }

    public void setEndlinenumber(int endLineNumber) {
        this.endLineNumber = endLineNumber;
    }


}