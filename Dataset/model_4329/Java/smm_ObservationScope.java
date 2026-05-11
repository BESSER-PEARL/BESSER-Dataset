





import java.util.List;
import java.util.ArrayList;

public class smm_ObservationScope extends SmmElement {

    private String scopeUri;





    private smm_Observation smm_observation;


    public smm_ObservationScope(
        String scopeUri    ) {
        super(
        );
        this.scopeUri = scopeUri;
    }


    public String getScopeuri() {
        return scopeUri;
    }

    public void setScopeuri(String scopeUri) {
        this.scopeUri = scopeUri;
    }

    public smm_Observation getSmm_observation() {
        return smm_observation;
    }

    public void setSmm_observation(smm_Observation smm_observation) {
        this.smm_observation = smm_observation;
    }

}