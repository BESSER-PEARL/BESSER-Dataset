





import java.util.List;
import java.util.ArrayList;

public class pcm_av_resourcetype_av_ResourceRepository  {






    private List<ResourceInterface> resourceinterfaces;




    private List<ResourceType> resourcetypes;


    public pcm_av_resourcetype_av_ResourceRepository(
    ) {
        this.resourceinterfaces = new ArrayList<>();
        this.resourcetypes = new ArrayList<>();
    }

    public pcm_av_resourcetype_av_ResourceRepository(
        ArrayList<ResourceInterface> resourceinterfaces,        ArrayList<ResourceType> resourcetypes    ) {
        this.resourceinterfaces = resourceinterfaces;
        this.resourcetypes = resourcetypes;
    }


    public List<ResourceInterface> getResourceinterfaces() {
        return resourceinterfaces;
    }

    public void addResourceinterface(Resourceinterface resourceinterface) {
        this.resourceinterfaces.add(resourceinterface);
    }
    public List<ResourceType> getResourcetypes() {
        return resourcetypes;
    }

    public void addResourcetype(Resourcetype resourcetype) {
        this.resourcetypes.add(resourcetype);
    }

}