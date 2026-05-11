





import java.util.List;
import java.util.ArrayList;

public class trace_DebugTraceRegion  {

    private int myEndOffset;
    private int myEndLineNumber;
    private int myLength;
    private boolean useForDebugging;
    private int myOffset;
    private String label;
    private int myLineNumber;





    private trace_DebugTraceRegion trace_debugtraceregion;


    public trace_DebugTraceRegion(
        int myEndOffset,        int myEndLineNumber,        int myLength,        boolean useForDebugging,        int myOffset,        String label,        int myLineNumber    ) {
        this.myEndOffset = myEndOffset;
        this.myEndLineNumber = myEndLineNumber;
        this.myLength = myLength;
        this.useForDebugging = useForDebugging;
        this.myOffset = myOffset;
        this.label = label;
        this.myLineNumber = myLineNumber;
    }


    public int getMyendoffset() {
        return myEndOffset;
    }

    public void setMyendoffset(int myEndOffset) {
        this.myEndOffset = myEndOffset;
    }
    public int getMyendlinenumber() {
        return myEndLineNumber;
    }

    public void setMyendlinenumber(int myEndLineNumber) {
        this.myEndLineNumber = myEndLineNumber;
    }
    public int getMylength() {
        return myLength;
    }

    public void setMylength(int myLength) {
        this.myLength = myLength;
    }
    public boolean getUsefordebugging() {
        return useForDebugging;
    }

    public void setUsefordebugging(boolean useForDebugging) {
        this.useForDebugging = useForDebugging;
    }
    public int getMyoffset() {
        return myOffset;
    }

    public void setMyoffset(int myOffset) {
        this.myOffset = myOffset;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public int getMylinenumber() {
        return myLineNumber;
    }

    public void setMylinenumber(int myLineNumber) {
        this.myLineNumber = myLineNumber;
    }

    public trace_DebugTraceRegion getTrace_debugtraceregion() {
        return trace_debugtraceregion;
    }

    public void setTrace_debugtraceregion(trace_DebugTraceRegion trace_debugtraceregion) {
        this.trace_debugtraceregion = trace_debugtraceregion;
    }

}