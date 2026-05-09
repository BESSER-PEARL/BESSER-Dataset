





import java.util.List;
import java.util.ArrayList;

public class oaam_library_ResourceProviderA  {






    private List<ResourceGroup> resourcegroups;


    public oaam_library_ResourceProviderA(
    ) {
        this.resourcegroups = new ArrayList<>();
    }

    public oaam_library_ResourceProviderA(
        ArrayList<ResourceGroup> resourcegroups    ) {
        this.resourcegroups = resourcegroups;
    }


    public List<ResourceGroup> getResourcegroups() {
        return resourcegroups;
    }

    public void addResourcegroup(Resourcegroup resourcegroup) {
        this.resourcegroups.add(resourcegroup);
    }

}