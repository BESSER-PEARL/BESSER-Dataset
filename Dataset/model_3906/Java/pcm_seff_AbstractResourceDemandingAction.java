





import java.util.List;
import java.util.ArrayList;

public class pcm_seff_AbstractResourceDemandingAction extends AbstractAction {






    private List<ParametricResourceDemand> parametricresourcedemands;


    public pcm_seff_AbstractResourceDemandingAction(
    ) {
        super(
        );
        this.parametricresourcedemands = new ArrayList<>();
    }

    public pcm_seff_AbstractResourceDemandingAction(
        ArrayList<ParametricResourceDemand> parametricresourcedemands    ) {
        this.parametricresourcedemands = parametricresourcedemands;
    }


    public List<ParametricResourceDemand> getParametricresourcedemands() {
        return parametricresourcedemands;
    }

    public void addParametricresourcedemand(Parametricresourcedemand parametricresourcedemand) {
        this.parametricresourcedemands.add(parametricresourcedemand);
    }

}