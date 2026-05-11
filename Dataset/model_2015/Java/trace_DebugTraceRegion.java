





import java.util.List;
import java.util.ArrayList;

public class trace_DebugTraceRegion  {

    private String label;
    private int myLength;
    private int myEndOffset;
    private int myOffset;
    private int myEndLineNumber;
    private int myLineNumber;





    private List<trace_DebugTraceRegion> trace_debugtraceregions;




    private List<trace_DebugLocationData> trace_debuglocationdatas;


    public trace_DebugTraceRegion(
        String label,        int myLength,        int myEndOffset,        int myOffset,        int myEndLineNumber,        int myLineNumber    ) {
        this.label = label;
        this.myLength = myLength;
        this.myEndOffset = myEndOffset;
        this.myOffset = myOffset;
        this.myEndLineNumber = myEndLineNumber;
        this.myLineNumber = myLineNumber;
        this.trace_debugtraceregions = new ArrayList<>();
        this.trace_debuglocationdatas = new ArrayList<>();
    }

    public trace_DebugTraceRegion(
        String label,        int myLength,        int myEndOffset,        int myOffset,        int myEndLineNumber,        int myLineNumber        ArrayList<trace_DebugTraceRegion> trace_debugtraceregions,        ArrayList<trace_DebugLocationData> trace_debuglocationdatas    ) {
        this.label = label;
        this.myLength = myLength;
        this.myEndOffset = myEndOffset;
        this.myOffset = myOffset;
        this.myEndLineNumber = myEndLineNumber;
        this.myLineNumber = myLineNumber;
        this.trace_debugtraceregions = trace_debugtraceregions;
        this.trace_debuglocationdatas = trace_debuglocationdatas;
    }

    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public int getMylength() {
        return myLength;
    }

    public void setMylength(int myLength) {
        this.myLength = myLength;
    }
    public int getMyendoffset() {
        return myEndOffset;
    }

    public void setMyendoffset(int myEndOffset) {
        this.myEndOffset = myEndOffset;
    }
    public int getMyoffset() {
        return myOffset;
    }

    public void setMyoffset(int myOffset) {
        this.myOffset = myOffset;
    }
    public int getMyendlinenumber() {
        return myEndLineNumber;
    }

    public void setMyendlinenumber(int myEndLineNumber) {
        this.myEndLineNumber = myEndLineNumber;
    }
    public int getMylinenumber() {
        return myLineNumber;
    }

    public void setMylinenumber(int myLineNumber) {
        this.myLineNumber = myLineNumber;
    }

    public List<trace_DebugTraceRegion> getTrace_debugtraceregions() {
        return trace_debugtraceregions;
    }

    public void addTrace_debugtraceregion(Trace_debugtraceregion trace_debugtraceregion) {
        this.trace_debugtraceregions.add(trace_debugtraceregion);
    }
    public List<trace_DebugLocationData> getTrace_debuglocationdatas() {
        return trace_debuglocationdatas;
    }

    public void addTrace_debuglocationdata(Trace_debuglocationdata trace_debuglocationdata) {
        this.trace_debuglocationdatas.add(trace_debuglocationdata);
    }

}