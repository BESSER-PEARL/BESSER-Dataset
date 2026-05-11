





import java.util.List;
import java.util.ArrayList;

public class traceability_Trace  {

    private String id;
    private String objects;





    private traceability_Traceability traceability_traceability;


    public traceability_Trace(
        String id,        String objects    ) {
        this.id = id;
        this.objects = objects;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getObjects() {
        return objects;
    }

    public void setObjects(String objects) {
        this.objects = objects;
    }

    public traceability_Traceability getTraceability_traceability() {
        return traceability_traceability;
    }

    public void setTraceability_traceability(traceability_Traceability traceability_traceability) {
        this.traceability_traceability = traceability_traceability;
    }

}