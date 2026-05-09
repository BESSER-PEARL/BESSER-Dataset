





import java.util.List;
import java.util.ArrayList;

public class TraceMetamodel_TraceLink  {

    private String name;
    private boolean isPartial;
    private String trule;
    private boolean isNonInjective;
    private String id;





    private TraceMetamodel_TraceModel tracemetamodel_tracemodel;


    public TraceMetamodel_TraceLink(
        String name,        boolean isPartial,        String trule,        boolean isNonInjective,        String id    ) {
        this.name = name;
        this.isPartial = isPartial;
        this.trule = trule;
        this.isNonInjective = isNonInjective;
        this.id = id;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getIspartial() {
        return isPartial;
    }

    public void setIspartial(boolean isPartial) {
        this.isPartial = isPartial;
    }
    public String getTrule() {
        return trule;
    }

    public void setTrule(String trule) {
        this.trule = trule;
    }
    public boolean getIsnoninjective() {
        return isNonInjective;
    }

    public void setIsnoninjective(boolean isNonInjective) {
        this.isNonInjective = isNonInjective;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public TraceMetamodel_TraceModel getTracemetamodel_tracemodel() {
        return tracemetamodel_tracemodel;
    }

    public void setTracemetamodel_tracemodel(TraceMetamodel_TraceModel tracemetamodel_tracemodel) {
        this.tracemetamodel_tracemodel = tracemetamodel_tracemodel;
    }

}