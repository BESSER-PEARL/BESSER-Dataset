





import java.util.List;
import java.util.ArrayList;

public class dependability2stochasticpetrinet_Dependability2StochasticPetriNetTrace  {






    private dependability2stochasticpetrinet_RailwayContainer dependability2stochasticpetrinet_railwaycontainer;




    private dependability2stochasticpetrinet_DependabilityModel dependability2stochasticpetrinet_dependabilitymodel;




    private List<dependability2stochasticpetrinet_TraceLink> dependability2stochasticpetrinet_tracelinks;


    public dependability2stochasticpetrinet_Dependability2StochasticPetriNetTrace(
    ) {
        this.dependability2stochasticpetrinet_tracelinks = new ArrayList<>();
    }

    public dependability2stochasticpetrinet_Dependability2StochasticPetriNetTrace(
        ArrayList<dependability2stochasticpetrinet_TraceLink> dependability2stochasticpetrinet_tracelinks    ) {
        this.dependability2stochasticpetrinet_tracelinks = dependability2stochasticpetrinet_tracelinks;
    }


    public dependability2stochasticpetrinet_RailwayContainer getDependability2stochasticpetrinet_railwaycontainer() {
        return dependability2stochasticpetrinet_railwaycontainer;
    }

    public void setDependability2stochasticpetrinet_railwaycontainer(dependability2stochasticpetrinet_RailwayContainer dependability2stochasticpetrinet_railwaycontainer) {
        this.dependability2stochasticpetrinet_railwaycontainer = dependability2stochasticpetrinet_railwaycontainer;
    }
    public dependability2stochasticpetrinet_DependabilityModel getDependability2stochasticpetrinet_dependabilitymodel() {
        return dependability2stochasticpetrinet_dependabilitymodel;
    }

    public void setDependability2stochasticpetrinet_dependabilitymodel(dependability2stochasticpetrinet_DependabilityModel dependability2stochasticpetrinet_dependabilitymodel) {
        this.dependability2stochasticpetrinet_dependabilitymodel = dependability2stochasticpetrinet_dependabilitymodel;
    }
    public List<dependability2stochasticpetrinet_TraceLink> getDependability2stochasticpetrinet_tracelinks() {
        return dependability2stochasticpetrinet_tracelinks;
    }

    public void addDependability2stochasticpetrinet_tracelink(Dependability2stochasticpetrinet_tracelink dependability2stochasticpetrinet_tracelink) {
        this.dependability2stochasticpetrinet_tracelinks.add(dependability2stochasticpetrinet_tracelink);
    }

}