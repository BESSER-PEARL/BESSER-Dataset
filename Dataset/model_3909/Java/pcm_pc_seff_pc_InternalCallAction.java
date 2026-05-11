





import java.util.List;
import java.util.ArrayList;

public class pcm_pc_seff_pc_InternalCallAction extends seff_pc_AbstractInternalControlFlowAction, seff_pc_CallAction {






    private ResourceDemandingInternalBehaviour resourcedemandinginternalbehaviour;


    public pcm_pc_seff_pc_InternalCallAction(
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