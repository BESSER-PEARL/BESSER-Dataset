





import java.util.List;
import java.util.ArrayList;

public class pcm_av_entity_av_ResourceInterfaceRequiringEntity extends Entity {






    private List<entity_av_ResourceRequiredRole> entity_av_resourcerequiredroles;


    public pcm_av_entity_av_ResourceInterfaceRequiringEntity(
    ) {
        super(
        );
        this.entity_av_resourcerequiredroles = new ArrayList<>();
    }

    public pcm_av_entity_av_ResourceInterfaceRequiringEntity(
        ArrayList<entity_av_ResourceRequiredRole> entity_av_resourcerequiredroles    ) {
        this.entity_av_resourcerequiredroles = entity_av_resourcerequiredroles;
    }


    public List<entity_av_ResourceRequiredRole> getEntity_av_resourcerequiredroles() {
        return entity_av_resourcerequiredroles;
    }

    public void addEntity_av_resourcerequiredrole(Entity_av_resourcerequiredrole entity_av_resourcerequiredrole) {
        this.entity_av_resourcerequiredroles.add(entity_av_resourcerequiredrole);
    }

}