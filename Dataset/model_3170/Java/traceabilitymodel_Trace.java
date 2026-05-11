





import java.util.List;
import java.util.ArrayList;

public class traceabilitymodel_Trace  {

    private String specificationName;
    private String sourceOperationName;
    private String sourceOperationID;





    private traceabilitymodel_ModelElementRef traceabilitymodel_modelelementref;




    private traceabilitymodel_TraceModel traceabilitymodel_tracemodel;


    public traceabilitymodel_Trace(
        String specificationName,        String sourceOperationName,        String sourceOperationID    ) {
        this.specificationName = specificationName;
        this.sourceOperationName = sourceOperationName;
        this.sourceOperationID = sourceOperationID;
    }


    public String getSpecificationname() {
        return specificationName;
    }

    public void setSpecificationname(String specificationName) {
        this.specificationName = specificationName;
    }
    public String getSourceoperationname() {
        return sourceOperationName;
    }

    public void setSourceoperationname(String sourceOperationName) {
        this.sourceOperationName = sourceOperationName;
    }
    public String getSourceoperationid() {
        return sourceOperationID;
    }

    public void setSourceoperationid(String sourceOperationID) {
        this.sourceOperationID = sourceOperationID;
    }

    public traceabilitymodel_ModelElementRef getTraceabilitymodel_modelelementref() {
        return traceabilitymodel_modelelementref;
    }

    public void setTraceabilitymodel_modelelementref(traceabilitymodel_ModelElementRef traceabilitymodel_modelelementref) {
        this.traceabilitymodel_modelelementref = traceabilitymodel_modelelementref;
    }
    public traceabilitymodel_TraceModel getTraceabilitymodel_tracemodel() {
        return traceabilitymodel_tracemodel;
    }

    public void setTraceabilitymodel_tracemodel(traceabilitymodel_TraceModel traceabilitymodel_tracemodel) {
        this.traceabilitymodel_tracemodel = traceabilitymodel_tracemodel;
    }

}