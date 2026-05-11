





import java.util.List;
import java.util.ArrayList;

public class traceability_EDFDGraphTrace  {






    private traceability_EDFDToGraph traceability_edfdtograph;




    private List<traceability_NamedEntity> traceability_namedentitys;


    public traceability_EDFDGraphTrace(
    ) {
        this.traceability_namedentitys = new ArrayList<>();
    }

    public traceability_EDFDGraphTrace(
        ArrayList<traceability_NamedEntity> traceability_namedentitys    ) {
        this.traceability_namedentitys = traceability_namedentitys;
    }


    public traceability_EDFDToGraph getTraceability_edfdtograph() {
        return traceability_edfdtograph;
    }

    public void setTraceability_edfdtograph(traceability_EDFDToGraph traceability_edfdtograph) {
        this.traceability_edfdtograph = traceability_edfdtograph;
    }
    public List<traceability_NamedEntity> getTraceability_namedentitys() {
        return traceability_namedentitys;
    }

    public void addTraceability_namedentity(Traceability_namedentity traceability_namedentity) {
        this.traceability_namedentitys.add(traceability_namedentity);
    }

}