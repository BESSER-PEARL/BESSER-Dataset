





import java.util.List;
import java.util.ArrayList;

public class ResourceInterface  {






    private pcm_pc_entity_pc_ResourceProvidedRole pcm_pc_entity_pc_resourceprovidedrole;




    private pcm_pc_entity_pc_ResourceRequiredRole pcm_pc_entity_pc_resourcerequiredrole;


    public ResourceInterface(
    ) {
    }



    public pcm_pc_entity_pc_ResourceProvidedRole getPcm_pc_entity_pc_resourceprovidedrole() {
        return pcm_pc_entity_pc_resourceprovidedrole;
    }

    public void setPcm_pc_entity_pc_resourceprovidedrole(pcm_pc_entity_pc_ResourceProvidedRole pcm_pc_entity_pc_resourceprovidedrole) {
        this.pcm_pc_entity_pc_resourceprovidedrole = pcm_pc_entity_pc_resourceprovidedrole;
    }
    public pcm_pc_entity_pc_ResourceRequiredRole getPcm_pc_entity_pc_resourcerequiredrole() {
        return pcm_pc_entity_pc_resourcerequiredrole;
    }

    public void setPcm_pc_entity_pc_resourcerequiredrole(pcm_pc_entity_pc_ResourceRequiredRole pcm_pc_entity_pc_resourcerequiredrole) {
        this.pcm_pc_entity_pc_resourcerequiredrole = pcm_pc_entity_pc_resourcerequiredrole;
    }

}