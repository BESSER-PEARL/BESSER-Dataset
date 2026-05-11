





import java.util.List;
import java.util.ArrayList;

public class pcm_seff_AcquireAction extends AbstractResourceDemandingAction {






    private PassiveResource passiveresource;


    public pcm_seff_AcquireAction(
    ) {
        super(
        );
    }



    public PassiveResource getPassiveresource() {
        return passiveresource;
    }

    public void setPassiveresource(PassiveResource passiveresource) {
        this.passiveresource = passiveresource;
    }

}