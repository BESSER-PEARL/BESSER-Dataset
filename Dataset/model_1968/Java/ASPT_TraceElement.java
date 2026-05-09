





import java.util.List;
import java.util.ArrayList;

public class ASPT_TraceElement  {

    private String type;
    private String idx;
    private String id;
    private String metamodel;





    private ASPT_TraceModel aspt_tracemodel;


    public ASPT_TraceElement(
        String type,        String idx,        String id,        String metamodel    ) {
        this.type = type;
        this.idx = idx;
        this.id = id;
        this.metamodel = metamodel;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getIdx() {
        return idx;
    }

    public void setIdx(String idx) {
        this.idx = idx;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getMetamodel() {
        return metamodel;
    }

    public void setMetamodel(String metamodel) {
        this.metamodel = metamodel;
    }

    public ASPT_TraceModel getAspt_tracemodel() {
        return aspt_tracemodel;
    }

    public void setAspt_tracemodel(ASPT_TraceModel aspt_tracemodel) {
        this.aspt_tracemodel = aspt_tracemodel;
    }

}