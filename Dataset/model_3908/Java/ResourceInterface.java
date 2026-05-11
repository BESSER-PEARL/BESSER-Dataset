





import java.util.List;
import java.util.ArrayList;

public class ResourceInterface  {






    private pcm_av_entity_av_ResourceProvidedRole pcm_av_entity_av_resourceprovidedrole;




    private pcm_av_entity_av_ResourceRequiredRole pcm_av_entity_av_resourcerequiredrole;


    public ResourceInterface(
    ) {
    }



    public pcm_av_entity_av_ResourceProvidedRole getPcm_av_entity_av_resourceprovidedrole() {
        return pcm_av_entity_av_resourceprovidedrole;
    }

    public void setPcm_av_entity_av_resourceprovidedrole(pcm_av_entity_av_ResourceProvidedRole pcm_av_entity_av_resourceprovidedrole) {
        this.pcm_av_entity_av_resourceprovidedrole = pcm_av_entity_av_resourceprovidedrole;
    }
    public pcm_av_entity_av_ResourceRequiredRole getPcm_av_entity_av_resourcerequiredrole() {
        return pcm_av_entity_av_resourcerequiredrole;
    }

    public void setPcm_av_entity_av_resourcerequiredrole(pcm_av_entity_av_ResourceRequiredRole pcm_av_entity_av_resourcerequiredrole) {
        this.pcm_av_entity_av_resourcerequiredrole = pcm_av_entity_av_resourcerequiredrole;
    }

}