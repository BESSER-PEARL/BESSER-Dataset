





import java.util.List;
import java.util.ArrayList;

public class pcm_av_pc_seff_av_pc_ResourceDemandingBehaviour extends Identifier {






    private List<AbstractAction> abstractactions;


    public pcm_av_pc_seff_av_pc_ResourceDemandingBehaviour(
    ) {
        super(
        );
        this.abstractactions = new ArrayList<>();
    }

    public pcm_av_pc_seff_av_pc_ResourceDemandingBehaviour(
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