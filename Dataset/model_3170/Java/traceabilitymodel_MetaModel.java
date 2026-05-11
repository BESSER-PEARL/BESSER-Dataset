





import java.util.List;
import java.util.ArrayList;

public class traceabilitymodel_MetaModel  {

    private String nsUri;
    private String name;





    private traceabilitymodel_TraceModel traceabilitymodel_tracemodel;




    private traceabilitymodel_ModelElementRef traceabilitymodel_modelelementref;


    public traceabilitymodel_MetaModel(
        String nsUri,        String name    ) {
        this.nsUri = nsUri;
        this.name = name;
    }


    public String getNsuri() {
        return nsUri;
    }

    public void setNsuri(String nsUri) {
        this.nsUri = nsUri;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public traceabilitymodel_TraceModel getTraceabilitymodel_tracemodel() {
        return traceabilitymodel_tracemodel;
    }

    public void setTraceabilitymodel_tracemodel(traceabilitymodel_TraceModel traceabilitymodel_tracemodel) {
        this.traceabilitymodel_tracemodel = traceabilitymodel_tracemodel;
    }
    public traceabilitymodel_ModelElementRef getTraceabilitymodel_modelelementref() {
        return traceabilitymodel_modelelementref;
    }

    public void setTraceabilitymodel_modelelementref(traceabilitymodel_ModelElementRef traceabilitymodel_modelelementref) {
        this.traceabilitymodel_modelelementref = traceabilitymodel_modelelementref;
    }

}