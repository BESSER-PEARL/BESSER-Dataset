





import java.util.List;
import java.util.ArrayList;

public class traces_Trace  {






    private List<traces_RootOut> traces_rootouts;


    public traces_Trace(
    ) {
        this.traces_rootouts = new ArrayList<>();
    }

    public traces_Trace(
        ArrayList<traces_RootOut> traces_rootouts    ) {
        this.traces_rootouts = traces_rootouts;
    }


    public List<traces_RootOut> getTraces_rootouts() {
        return traces_rootouts;
    }

    public void addTraces_rootout(Traces_rootout traces_rootout) {
        this.traces_rootouts.add(traces_rootout);
    }

}