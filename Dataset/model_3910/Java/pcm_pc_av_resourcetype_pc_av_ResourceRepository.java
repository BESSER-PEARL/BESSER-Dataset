





import java.util.List;
import java.util.ArrayList;

public class pcm_pc_av_resourcetype_pc_av_ResourceRepository  {






    private List<ResourceInterface> resourceinterfaces;


    public pcm_pc_av_resourcetype_pc_av_ResourceRepository(
    ) {
        this.resourceinterfaces = new ArrayList<>();
    }

    public pcm_pc_av_resourcetype_pc_av_ResourceRepository(
        ArrayList<ResourceInterface> resourceinterfaces    ) {
        this.resourceinterfaces = resourceinterfaces;
    }


    public List<ResourceInterface> getResourceinterfaces() {
        return resourceinterfaces;
    }

    public void addResourceinterface(Resourceinterface resourceinterface) {
        this.resourceinterfaces.add(resourceinterface);
    }

}