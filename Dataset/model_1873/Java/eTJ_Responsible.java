





import java.util.List;
import java.util.ArrayList;

public class eTJ_Responsible  {






    private List<eTJ_Resource> etj_resources;


    public eTJ_Responsible(
    ) {
        this.etj_resources = new ArrayList<>();
    }

    public eTJ_Responsible(
        ArrayList<eTJ_Resource> etj_resources    ) {
        this.etj_resources = etj_resources;
    }


    public List<eTJ_Resource> getEtj_resources() {
        return etj_resources;
    }

    public void addEtj_resource(Etj_resource etj_resource) {
        this.etj_resources.add(etj_resource);
    }

}