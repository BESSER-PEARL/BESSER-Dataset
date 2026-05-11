





import java.util.List;
import java.util.ArrayList;

public class pcm_av_pc_resourcetype_av_pc_ResourceRepository  {






    private List<ResourceType> resourcetypes;


    public pcm_av_pc_resourcetype_av_pc_ResourceRepository(
    ) {
        this.resourcetypes = new ArrayList<>();
    }

    public pcm_av_pc_resourcetype_av_pc_ResourceRepository(
        ArrayList<ResourceType> resourcetypes    ) {
        this.resourcetypes = resourcetypes;
    }


    public List<ResourceType> getResourcetypes() {
        return resourcetypes;
    }

    public void addResourcetype(Resourcetype resourcetype) {
        this.resourcetypes.add(resourcetype);
    }

}