





import java.util.List;
import java.util.ArrayList;

public class ResourceInterface  {






    private pcm_av_pc_entity_av_pc_ResourceRequiredRole pcm_av_pc_entity_av_pc_resourcerequiredrole;




    private pcm_av_pc_entity_av_pc_ResourceProvidedRole pcm_av_pc_entity_av_pc_resourceprovidedrole;




    private pcm_av_pc_resourcetype_av_pc_ResourceSignature pcm_av_pc_resourcetype_av_pc_resourcesignature;




    private pcm_av_pc_resourcetype_av_pc_ResourceRepository pcm_av_pc_resourcetype_av_pc_resourcerepository;


    public ResourceInterface(
    ) {
    }



    public pcm_av_pc_entity_av_pc_ResourceRequiredRole getPcm_av_pc_entity_av_pc_resourcerequiredrole() {
        return pcm_av_pc_entity_av_pc_resourcerequiredrole;
    }

    public void setPcm_av_pc_entity_av_pc_resourcerequiredrole(pcm_av_pc_entity_av_pc_ResourceRequiredRole pcm_av_pc_entity_av_pc_resourcerequiredrole) {
        this.pcm_av_pc_entity_av_pc_resourcerequiredrole = pcm_av_pc_entity_av_pc_resourcerequiredrole;
    }
    public pcm_av_pc_entity_av_pc_ResourceProvidedRole getPcm_av_pc_entity_av_pc_resourceprovidedrole() {
        return pcm_av_pc_entity_av_pc_resourceprovidedrole;
    }

    public void setPcm_av_pc_entity_av_pc_resourceprovidedrole(pcm_av_pc_entity_av_pc_ResourceProvidedRole pcm_av_pc_entity_av_pc_resourceprovidedrole) {
        this.pcm_av_pc_entity_av_pc_resourceprovidedrole = pcm_av_pc_entity_av_pc_resourceprovidedrole;
    }
    public pcm_av_pc_resourcetype_av_pc_ResourceSignature getPcm_av_pc_resourcetype_av_pc_resourcesignature() {
        return pcm_av_pc_resourcetype_av_pc_resourcesignature;
    }

    public void setPcm_av_pc_resourcetype_av_pc_resourcesignature(pcm_av_pc_resourcetype_av_pc_ResourceSignature pcm_av_pc_resourcetype_av_pc_resourcesignature) {
        this.pcm_av_pc_resourcetype_av_pc_resourcesignature = pcm_av_pc_resourcetype_av_pc_resourcesignature;
    }
    public pcm_av_pc_resourcetype_av_pc_ResourceRepository getPcm_av_pc_resourcetype_av_pc_resourcerepository() {
        return pcm_av_pc_resourcetype_av_pc_resourcerepository;
    }

    public void setPcm_av_pc_resourcetype_av_pc_resourcerepository(pcm_av_pc_resourcetype_av_pc_ResourceRepository pcm_av_pc_resourcetype_av_pc_resourcerepository) {
        this.pcm_av_pc_resourcetype_av_pc_resourcerepository = pcm_av_pc_resourcetype_av_pc_resourcerepository;
    }

}