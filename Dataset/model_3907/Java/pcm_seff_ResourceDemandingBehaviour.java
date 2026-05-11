





import java.util.List;
import java.util.ArrayList;

public class pcm_seff_ResourceDemandingBehaviour  {






    private List<AbstractAction> abstractactions;


    public pcm_seff_ResourceDemandingBehaviour(
    ) {
        this.abstractactions = new ArrayList<>();
    }

    public pcm_seff_ResourceDemandingBehaviour(
        ArrayList<AbstractAction> abstractactions    ) {
        this.abstractactions = abstractactions;
    }


    public List<AbstractAction> getAbstractactions() {
        return abstractactions;
    }

    public void addAbstractaction(Abstractaction abstractaction) {
        this.abstractactions.add(abstractaction);
    }

}