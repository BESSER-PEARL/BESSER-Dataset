





import java.util.List;
import java.util.ArrayList;

public class oaam_library_ResourceConsumerA  {






    private List<Resource> resources;




    private List<ResourceGroup> resourcegroups;


    public oaam_library_ResourceConsumerA(
    ) {
        this.resources = new ArrayList<>();
        this.resourcegroups = new ArrayList<>();
    }

    public oaam_library_ResourceConsumerA(
        ArrayList<Resource> resources,        ArrayList<ResourceGroup> resourcegroups    ) {
        this.resources = resources;
        this.resourcegroups = resourcegroups;
    }


    public List<Resource> getResources() {
        return resources;
    }

    public void addResource(Resource resource) {
        this.resources.add(resource);
    }
    public List<ResourceGroup> getResourcegroups() {
        return resourcegroups;
    }

    public void addResourcegroup(Resourcegroup resourcegroup) {
        this.resourcegroups.add(resourcegroup);
    }

}