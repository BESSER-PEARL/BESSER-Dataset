





import java.util.List;
import java.util.ArrayList;

public class analysis_trace_ComparedTrace  {

    private String dSteps;
    private boolean equal;
    private String dDependencies;





    private List<trace_analysis_Action> trace_analysis_actions;




    private CompressedTraceReport compressedtracereport;


    public analysis_trace_ComparedTrace(
        String dSteps,        boolean equal,        String dDependencies    ) {
        this.dSteps = dSteps;
        this.equal = equal;
        this.dDependencies = dDependencies;
        this.trace_analysis_actions = new ArrayList<>();
    }

    public analysis_trace_ComparedTrace(
        String dSteps,        boolean equal,        String dDependencies        ArrayList<trace_analysis_Action> trace_analysis_actions    ) {
        this.dSteps = dSteps;
        this.equal = equal;
        this.dDependencies = dDependencies;
        this.trace_analysis_actions = trace_analysis_actions;
    }

    public String getDsteps() {
        return dSteps;
    }

    public void setDsteps(String dSteps) {
        this.dSteps = dSteps;
    }
    public boolean getEqual() {
        return equal;
    }

    public void setEqual(boolean equal) {
        this.equal = equal;
    }
    public String getDdependencies() {
        return dDependencies;
    }

    public void setDdependencies(String dDependencies) {
        this.dDependencies = dDependencies;
    }

    public List<trace_analysis_Action> getTrace_analysis_actions() {
        return trace_analysis_actions;
    }

    public void addTrace_analysis_action(Trace_analysis_action trace_analysis_action) {
        this.trace_analysis_actions.add(trace_analysis_action);
    }
    public CompressedTraceReport getCompressedtracereport() {
        return compressedtracereport;
    }

    public void setCompressedtracereport(CompressedTraceReport compressedtracereport) {
        this.compressedtracereport = compressedtracereport;
    }

}