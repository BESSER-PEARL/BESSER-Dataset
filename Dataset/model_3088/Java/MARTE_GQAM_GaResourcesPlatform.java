





import java.util.List;
import java.util.ArrayList;

public class MARTE_GQAM_GaResourcesPlatform  {






    private List<GRM_Resource> grm_resources;


    public MARTE_GQAM_GaResourcesPlatform(
    ) {
        this.grm_resources = new ArrayList<>();
    }

    public MARTE_GQAM_GaResourcesPlatform(
        ArrayList<GRM_Resource> grm_resources    ) {
        this.grm_resources = grm_resources;
    }


    public List<GRM_Resource> getGrm_resources() {
        return grm_resources;
    }

    public void addGrm_resource(Grm_resource grm_resource) {
        this.grm_resources.add(grm_resource);
    }

}