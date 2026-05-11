





import java.util.List;
import java.util.ArrayList;

public class pcm_av_seff_av_InternalCallAction extends seff_av_CallAction, seff_av_AbstractInternalControlFlowAction {






    private ResourceDemandingInternalBehaviour resourcedemandinginternalbehaviour;


    public pcm_av_seff_av_InternalCallAction(
    ) {
        super(
        );
    }



    public ResourceDemandingInternalBehaviour getResourcedemandinginternalbehaviour() {
        return resourcedemandinginternalbehaviour;
    }

    public void setResourcedemandinginternalbehaviour(ResourceDemandingInternalBehaviour resourcedemandinginternalbehaviour) {
        this.resourcedemandinginternalbehaviour = resourcedemandinginternalbehaviour;
    }

}