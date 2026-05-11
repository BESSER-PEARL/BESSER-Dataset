





import java.util.List;
import java.util.ArrayList;

public class smm_SmmModel extends SmmElement {






    private List<smm_Observation> smm_observations;


    public smm_SmmModel(
    ) {
        super(
        );
        this.smm_observations = new ArrayList<>();
    }

    public smm_SmmModel(
        ArrayList<smm_Observation> smm_observations    ) {
        this.smm_observations = smm_observations;
    }


    public List<smm_Observation> getSmm_observations() {
        return smm_observations;
    }

    public void addSmm_observation(Smm_observation smm_observation) {
        this.smm_observations.add(smm_observation);
    }

}