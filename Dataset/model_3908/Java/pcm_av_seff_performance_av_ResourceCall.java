





import java.util.List;
import java.util.ArrayList;

public class pcm_av_seff_performance_av_ResourceCall extends CallAction {






    private ResourceSignature resourcesignature;




    private PCMRandomVariable pcmrandomvariable;




    private entity_av_ResourceRequiredRole entity_av_resourcerequiredrole;


    public pcm_av_seff_performance_av_ResourceCall(
    ) {
        super(
        );
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
    public entity_av_ResourceRequiredRole getEntity_av_resourcerequiredrole() {
        return entity_av_resourcerequiredrole;
    }

    public void setEntity_av_resourcerequiredrole(entity_av_ResourceRequiredRole entity_av_resourcerequiredrole) {
        this.entity_av_resourcerequiredrole = entity_av_resourcerequiredrole;
    }

}