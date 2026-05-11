





import java.util.List;
import java.util.ArrayList;

public class traceability_DiffCategory  {

    private String name;
    private int modelIndex;
    private boolean unequal;





    private List<traceability_TraceDiff> traceability_tracediffs;


    public traceability_DiffCategory(
        String name,        int modelIndex,        boolean unequal    ) {
        this.name = name;
        this.modelIndex = modelIndex;
        this.unequal = unequal;
        this.traceability_tracediffs = new ArrayList<>();
    }

    public traceability_DiffCategory(
        String name,        int modelIndex,        boolean unequal        ArrayList<traceability_TraceDiff> traceability_tracediffs    ) {
        this.name = name;
        this.modelIndex = modelIndex;
        this.unequal = unequal;
        this.traceability_tracediffs = traceability_tracediffs;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getModelindex() {
        return modelIndex;
    }

    public void setModelindex(int modelIndex) {
        this.modelIndex = modelIndex;
    }
    public boolean getUnequal() {
        return unequal;
    }

    public void setUnequal(boolean unequal) {
        this.unequal = unequal;
    }

    public List<traceability_TraceDiff> getTraceability_tracediffs() {
        return traceability_tracediffs;
    }

    public void addTraceability_tracediff(Traceability_tracediff traceability_tracediff) {
        this.traceability_tracediffs.add(traceability_tracediff);
    }

}