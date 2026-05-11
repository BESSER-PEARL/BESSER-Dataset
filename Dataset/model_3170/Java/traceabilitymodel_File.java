





import java.util.List;
import java.util.ArrayList;

public class traceabilitymodel_File  {

    private String URI;
    private String name;
    private String ID;





    private traceabilitymodel_TraceModel traceabilitymodel_tracemodel;


    public traceabilitymodel_File(
        String URI,        String name,        String ID    ) {
        this.URI = URI;
        this.name = name;
        this.ID = ID;
    }


    public String getUri() {
        return URI;
    }

    public void setUri(String URI) {
        this.URI = URI;
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