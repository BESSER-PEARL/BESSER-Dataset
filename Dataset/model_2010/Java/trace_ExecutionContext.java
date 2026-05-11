





import java.util.List;
import java.util.ArrayList;

public class trace_ExecutionContext extends TraceElement {

    private String scriptId;
    private String modelsIds;





    private List<trace_Trace> trace_traces;




    private List<trace_ModelElement> trace_modelelements;




    private trace_Trace trace_trace;




    private trace_ModelElement trace_modelelement;




    private trace_ModuleElement trace_moduleelement;




    private List<trace_ModuleElement> trace_moduleelements;


    public trace_ExecutionContext(
        String scriptId,        String modelsIds    ) {
        super(
        );
        this.scriptId = scriptId;
        this.modelsIds = modelsIds;
        this.trace_traces = new ArrayList<>();
        this.trace_modelelements = new ArrayList<>();
        this.trace_moduleelements = new ArrayList<>();
    }

    public trace_ExecutionContext(
        String scriptId,        String modelsIds        ArrayList<trace_Trace> trace_traces,        ArrayList<trace_ModelElement> trace_modelelements,        ArrayList<trace_ModuleElement> trace_moduleelements    ) {
        this.scriptId = scriptId;
        this.modelsIds = modelsIds;
        this.trace_traces = trace_traces;
        this.trace_modelelements = trace_modelelements;
        this.trace_moduleelements = trace_moduleelements;
    }

    public String getScriptid() {
        return scriptId;
    }

    public void setScriptid(String scriptId) {
        this.scriptId = scriptId;
    }
    public String getModelsids() {
        return modelsIds;
    }

    public void setModelsids(String modelsIds) {
        this.modelsIds = modelsIds;
    }

    public List<trace_Trace> getTrace_traces() {
        return trace_traces;
    }

    public void addTrace_trace(Trace_trace trace_trace) {
        this.trace_traces.add(trace_trace);
    }
    public List<trace_ModelElement> getTrace_modelelements() {
        return trace_modelelements;
    }

    public void addTrace_modelelement(Trace_modelelement trace_modelelement) {
        this.trace_modelelements.add(trace_modelelement);
    }
    public trace_Trace getTrace_trace() {
        return trace_trace;
    }

    public void setTrace_trace(trace_Trace trace_trace) {
        this.trace_trace = trace_trace;
    }
    public trace_ModelElement getTrace_modelelement() {
        return trace_modelelement;
    }

    public void setTrace_modelelement(trace_ModelElement trace_modelelement) {
        this.trace_modelelement = trace_modelelement;
    }
    public trace_ModuleElement getTrace_moduleelement() {
        return trace_moduleelement;
    }

    public void setTrace_moduleelement(trace_ModuleElement trace_moduleelement) {
        this.trace_moduleelement = trace_moduleelement;
    }
    public List<trace_ModuleElement> getTrace_moduleelements() {
        return trace_moduleelements;
    }

    public void addTrace_moduleelement(Trace_moduleelement trace_moduleelement) {
        this.trace_moduleelements.add(trace_moduleelement);
    }

}