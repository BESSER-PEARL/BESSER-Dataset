





import java.util.List;
import java.util.ArrayList;

public class trace_Trace extends TraceElement {






    private trace_ModuleElement trace_moduleelement;




    private List<trace_ModelElement> trace_modelelements;




    private List<trace_Property> trace_propertys;




    private trace_ModuleElement trace_moduleelement;




    private trace_Property trace_property;




    private trace_ModelElement trace_modelelement;


    public trace_Trace(
    ) {
        super(
        );
        this.trace_modelelements = new ArrayList<>();
        this.trace_propertys = new ArrayList<>();
    }

    public trace_Trace(
        ArrayList<trace_ModelElement> trace_modelelements,        ArrayList<trace_Property> trace_propertys    ) {
        this.trace_modelelements = trace_modelelements;
        this.trace_propertys = trace_propertys;
    }


    public trace_ModuleElement getTrace_moduleelement() {
        return trace_moduleelement;
    }

    public void setTrace_moduleelement(trace_ModuleElement trace_moduleelement) {
        this.trace_moduleelement = trace_moduleelement;
    }
    public List<trace_ModelElement> getTrace_modelelements() {
        return trace_modelelements;
    }

    public void addTrace_modelelement(Trace_modelelement trace_modelelement) {
        this.trace_modelelements.add(trace_modelelement);
    }
    public List<trace_Property> getTrace_propertys() {
        return trace_propertys;
    }

    public void addTrace_property(Trace_property trace_property) {
        this.trace_propertys.add(trace_property);
    }
    public trace_ModuleElement getTrace_moduleelement() {
        return trace_moduleelement;
    }

    public void setTrace_moduleelement(trace_ModuleElement trace_moduleelement) {
        this.trace_moduleelement = trace_moduleelement;
    }
    public trace_Property getTrace_property() {
        return trace_property;
    }

    public void setTrace_property(trace_Property trace_property) {
        this.trace_property = trace_property;
    }
    public trace_ModelElement getTrace_modelelement() {
        return trace_modelelement;
    }

    public void setTrace_modelelement(trace_ModelElement trace_modelelement) {
        this.trace_modelelement = trace_modelelement;
    }

}