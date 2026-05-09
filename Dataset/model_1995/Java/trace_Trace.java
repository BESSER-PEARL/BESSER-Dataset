





import java.util.List;
import java.util.ArrayList;

public class trace_Trace  {






    private trace_EClass trace_eclass;




    private List<trace_ReferenceMapping> trace_referencemappings;




    private trace_EClass trace_eclass;




    private List<trace_AttributeMapping> trace_attributemappings;




    private List<trace_ClassMapping> trace_classmappings;


    public trace_Trace(
    ) {
        this.trace_referencemappings = new ArrayList<>();
        this.trace_attributemappings = new ArrayList<>();
        this.trace_classmappings = new ArrayList<>();
    }

    public trace_Trace(
        ArrayList<trace_ReferenceMapping> trace_referencemappings,        ArrayList<trace_AttributeMapping> trace_attributemappings,        ArrayList<trace_ClassMapping> trace_classmappings    ) {
        this.trace_referencemappings = trace_referencemappings;
        this.trace_attributemappings = trace_attributemappings;
        this.trace_classmappings = trace_classmappings;
    }


    public trace_EClass getTrace_eclass() {
        return trace_eclass;
    }

    public void setTrace_eclass(trace_EClass trace_eclass) {
        this.trace_eclass = trace_eclass;
    }
    public List<trace_ReferenceMapping> getTrace_referencemappings() {
        return trace_referencemappings;
    }

    public void addTrace_referencemapping(Trace_referencemapping trace_referencemapping) {
        this.trace_referencemappings.add(trace_referencemapping);
    }
    public trace_EClass getTrace_eclass() {
        return trace_eclass;
    }

    public void setTrace_eclass(trace_EClass trace_eclass) {
        this.trace_eclass = trace_eclass;
    }
    public List<trace_AttributeMapping> getTrace_attributemappings() {
        return trace_attributemappings;
    }

    public void addTrace_attributemapping(Trace_attributemapping trace_attributemapping) {
        this.trace_attributemappings.add(trace_attributemapping);
    }
    public List<trace_ClassMapping> getTrace_classmappings() {
        return trace_classmappings;
    }

    public void addTrace_classmapping(Trace_classmapping trace_classmapping) {
        this.trace_classmappings.add(trace_classmapping);
    }

}