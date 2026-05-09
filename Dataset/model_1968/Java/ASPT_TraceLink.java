





import java.util.List;
import java.util.ArrayList;

public class ASPT_TraceLink extends TraceElement {

    private String relation;
    private String idrefx;
    private String idref;





    private ASPT_TraceModel aspt_tracemodel;


    public ASPT_TraceLink(
        String relation,        String idrefx,        String idref    ) {
        super(
        );
        this.relation = relation;
        this.idrefx = idrefx;
        this.idref = idref;
    }


    public String getRelation() {
        return relation;
    }

    public void setRelation(String relation) {
        this.relation = relation;
    }
    public String getIdrefx() {
        return idrefx;
    }

    public void setIdrefx(String idrefx) {
        this.idrefx = idrefx;
    }
    public String getIdref() {
        return idref;
    }

    public void setIdref(String idref) {
        this.idref = idref;
    }

    public ASPT_TraceModel getAspt_tracemodel() {
        return aspt_tracemodel;
    }

    public void setAspt_tracemodel(ASPT_TraceModel aspt_tracemodel) {
        this.aspt_tracemodel = aspt_tracemodel;
    }

}