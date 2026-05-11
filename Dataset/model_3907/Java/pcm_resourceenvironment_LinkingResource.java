





import java.util.List;
import java.util.ArrayList;

public class pcm_resourceenvironment_LinkingResource extends Entity {






    private List<ResourceContainer> resourcecontainers;




    private List<ResourceContainer> resourcecontainers;


    public pcm_resourceenvironment_LinkingResource(
    ) {
        super(
        );
        this.resourcecontainers = new ArrayList<>();
        this.resourcecontainers = new ArrayList<>();
    }

    public pcm_resourceenvironment_LinkingResource(
        ArrayList<ResourceContainer> resourcecontainers,        ArrayList<ResourceContainer> resourcecontainers    ) {
        this.resourcecontainers = resourcecontainers;
        this.resourcecontainers = resourcecontainers;
    }


    public List<ResourceContainer> getResourcecontainers() {
        return resourcecontainers;
    }

    public void addResourcecontainer(Resourcecontainer resourcecontainer) {
        this.resourcecontainers.add(resourcecontainer);
    }
    public List<ResourceContainer> getResourcecontainers() {
        return resourcecontainers;
    }

    public void addResourcecontainer(Resourcecontainer resourcecontainer) {
        this.resourcecontainers.add(resourcecontainer);
    }

}