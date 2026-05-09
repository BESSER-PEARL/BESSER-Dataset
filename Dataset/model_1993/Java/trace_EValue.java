





import java.util.List;
import java.util.ArrayList;

public class trace_EValue  {

    private String collectionType;
    private String oclObject;
    private String primitiveValue;





    private trace_VarParameterValue trace_varparametervalue;




    private trace_EObject trace_eobject;




    private trace_EValue trace_evalue;




    private trace_ETuplePartValue trace_etuplepartvalue;




    private trace_EObject trace_eobject;


    public trace_EValue(
        String collectionType,        String oclObject,        String primitiveValue    ) {
        this.collectionType = collectionType;
        this.oclObject = oclObject;
        this.primitiveValue = primitiveValue;
    }


    public String getCollectiontype() {
        return collectionType;
    }

    public void setCollectiontype(String collectionType) {
        this.collectionType = collectionType;
    }
    public String getOclobject() {
        return oclObject;
    }

    public void setOclobject(String oclObject) {
        this.oclObject = oclObject;
    }
    public String getPrimitivevalue() {
        return primitiveValue;
    }

    public void setPrimitivevalue(String primitiveValue) {
        this.primitiveValue = primitiveValue;
    }

    public trace_VarParameterValue getTrace_varparametervalue() {
        return trace_varparametervalue;
    }

    public void setTrace_varparametervalue(trace_VarParameterValue trace_varparametervalue) {
        this.trace_varparametervalue = trace_varparametervalue;
    }
    public trace_EObject getTrace_eobject() {
        return trace_eobject;
    }

    public void setTrace_eobject(trace_EObject trace_eobject) {
        this.trace_eobject = trace_eobject;
    }
    public trace_EValue getTrace_evalue() {
        return trace_evalue;
    }

    public void setTrace_evalue(trace_EValue trace_evalue) {
        this.trace_evalue = trace_evalue;
    }
    public trace_ETuplePartValue getTrace_etuplepartvalue() {
        return trace_etuplepartvalue;
    }

    public void setTrace_etuplepartvalue(trace_ETuplePartValue trace_etuplepartvalue) {
        this.trace_etuplepartvalue = trace_etuplepartvalue;
    }
    public trace_EObject getTrace_eobject() {
        return trace_eobject;
    }

    public void setTrace_eobject(trace_EObject trace_eobject) {
        this.trace_eobject = trace_eobject;
    }

}