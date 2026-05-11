





import java.util.List;
import java.util.ArrayList;

public class traceabilitymodel_ModelElementRef  {

    private String uri;
    private String featureRef;
    private String name;
    private String ID;





    private traceabilitymodel_TraceModel traceabilitymodel_tracemodel;


    public traceabilitymodel_ModelElementRef(
        String uri,        String featureRef,        String name,        String ID    ) {
        this.uri = uri;
        this.featureRef = featureRef;
        this.name = name;
        this.ID = ID;
    }


    public String getUri() {
        return uri;
    }

    public void setUri(String uri) {
        this.uri = uri;
    }
    public String getFeatureref() {
        return featureRef;
    }

    public void setFeatureref(String featureRef) {
        this.featureRef = featureRef;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }

    public traceabilitymodel_TraceModel getTraceabilitymodel_tracemodel() {
        return traceabilitymodel_tracemodel;
    }

    public void setTraceabilitymodel_tracemodel(traceabilitymodel_TraceModel traceabilitymodel_tracemodel) {
        this.traceabilitymodel_tracemodel = traceabilitymodel_tracemodel;
    }

}