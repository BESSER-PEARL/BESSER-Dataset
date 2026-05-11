





import java.util.List;
import java.util.ArrayList;

public class pcm_resourceenvironment_ResourceEnvironment  {






    private List<ResourceContainer> resourcecontainers;


    public pcm_resourceenvironment_ResourceEnvironment(
    ) {
        this.resourcecontainers = new ArrayList<>();
    }

    public pcm_resourceenvironment_ResourceEnvironment(
        ArrayList<ResourceContainer> resourcecontainers    ) {
        this.resourcecontainers = resourcecontainers;
    }


    public List<ResourceContainer> getResourcecontainers() {
        return resourcecontainers;
    }

    public void addResourcecontainer(Resourcecontainer resourcecontainer) {
        this.resourcecontainers.add(resourcecontainer);
    }

}