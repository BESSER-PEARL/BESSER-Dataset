





import java.util.List;
import java.util.ArrayList;

public class trace_Slice extends EModelElement {

    private String kindLabel;
    private String name;
    private String kind;





    private trace_Slice trace_slice;




    private trace_Trace trace_trace;




    private List<trace_Slice> trace_slices;




    private trace_Slice trace_slice;


    public trace_Slice(
        String kindLabel,        String name,        String kind    ) {
        super(
        );
        this.kindLabel = kindLabel;
        this.name = name;
        this.kind = kind;
        this.trace_slices = new ArrayList<>();
    }

    public trace_Slice(
        String kindLabel,        String name,        String kind        ArrayList<trace_Slice> trace_slices    ) {
        this.kindLabel = kindLabel;
        this.name = name;
        this.kind = kind;
        this.trace_slices = trace_slices;
    }

    public String getKindlabel() {
        return kindLabel;
    }

    public void setKindlabel(String kindLabel) {
        this.kindLabel = kindLabel;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public trace_Slice getTrace_slice() {
        return trace_slice;
    }

    public void setTrace_slice(trace_Slice trace_slice) {
        this.trace_slice = trace_slice;
    }
    public trace_Trace getTrace_trace() {
        return trace_trace;
    }

    public void setTrace_trace(trace_Trace trace_trace) {
        this.trace_trace = trace_trace;
    }
    public List<trace_Slice> getTrace_slices() {
        return trace_slices;
    }

    public void addTrace_slice(Trace_slice trace_slice) {
        this.trace_slices.add(trace_slice);
    }
    public trace_Slice getTrace_slice() {
        return trace_slice;
    }

    public void setTrace_slice(trace_Slice trace_slice) {
        this.trace_slice = trace_slice;
    }

}