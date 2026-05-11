





import java.util.List;
import java.util.ArrayList;

public class pcm_pc_pc_resourcetype_pc_pc_ResourceRepository  {






    private List<ResourceType> resourcetypes;




    private List<ResourceInterface> resourceinterfaces;


    public pcm_pc_pc_resourcetype_pc_pc_ResourceRepository(
    ) {
        this.resourcetypes = new ArrayList<>();
        this.resourceinterfaces = new ArrayList<>();
    }

    public pcm_pc_pc_resourcetype_pc_pc_ResourceRepository(
        ArrayList<ResourceType> resourcetypes,        ArrayList<ResourceInterface> resourceinterfaces    ) {
        this.resourcetypes = resourcetypes;
        this.resourceinterfaces = resourceinterfaces;
    }


    public List<ResourceType> getResourcetypes() {
        return resourcetypes;
    }

    public void addResourcetype(Resourcetype resourcetype) {
        this.resourcetypes.add(resourcetype);
    }
    public List<ResourceInterface> getResourceinterfaces() {
        return resourceinterfaces;
    }

    public void addResourceinterface(Resourceinterface resourceinterface) {
        this.resourceinterfaces.add(resourceinterface);
    }

}