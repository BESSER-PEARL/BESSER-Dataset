





import java.util.List;
import java.util.ArrayList;

public class traceability_TraceDiffs  {






    private List<traceability_Traces> traceability_tracess;


    public traceability_TraceDiffs(
    ) {
        this.traceability_tracess = new ArrayList<>();
    }

    public traceability_TraceDiffs(
        ArrayList<traceability_Traces> traceability_tracess    ) {
        this.traceability_tracess = traceability_tracess;
    }


    public List<traceability_Traces> getTraceability_tracess() {
        return traceability_tracess;
    }

    public void addTraceability_traces(Traceability_traces traceability_traces) {
        this.traceability_tracess.add(traceability_traces);
    }

}