





import java.util.List;
import java.util.ArrayList;

public class pcm_pc_seff_performance_pc_ResourceCall extends CallAction {






    private entity_pc_ResourceRequiredRole entity_pc_resourcerequiredrole;




    private ResourceSignature resourcesignature;




    private PCMRandomVariable pcmrandomvariable;


    public pcm_pc_seff_performance_pc_ResourceCall(
    ) {
        super(
        );
    }



    public entity_pc_ResourceRequiredRole getEntity_pc_resourcerequiredrole() {
        return entity_pc_resourcerequiredrole;
    }

    public void setEntity_pc_resourcerequiredrole(entity_pc_ResourceRequiredRole entity_pc_resourcerequiredrole) {
        this.entity_pc_resourcerequiredrole = entity_pc_resourcerequiredrole;
    }
    public ResourceSignature getResourcesignature() {
        return resourcesignature;
    }

    public void setResourcesignature(ResourceSignature resourcesignature) {
        this.resourcesignature = resourcesignature;
    }
    public PCMRandomVariable getPcmrandomvariable() {
        return pcmrandomvariable;
    }

    public void setPcmrandomvariable(PCMRandomVariable pcmrandomvariable) {
        this.pcmrandomvariable = pcmrandomvariable;
    }

}