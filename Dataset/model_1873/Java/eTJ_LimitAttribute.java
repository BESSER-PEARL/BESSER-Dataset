





import java.util.List;
import java.util.ArrayList;

public class eTJ_LimitAttribute  {






    private List<eTJ_Resource> etj_resources;




    private eTJ_Limit etj_limit;


    public eTJ_LimitAttribute(
    ) {
        this.etj_resources = new ArrayList<>();
    }

    public eTJ_LimitAttribute(
        ArrayList<eTJ_Resource> etj_resources    ) {
        this.etj_resources = etj_resources;
    }


    public List<eTJ_Resource> getEtj_resources() {
        return etj_resources;
    }

    public void addEtj_resource(Etj_resource etj_resource) {
        this.etj_resources.add(etj_resource);
    }
    public eTJ_Limit getEtj_limit() {
        return etj_limit;
    }

    public void setEtj_limit(eTJ_Limit etj_limit) {
        this.etj_limit = etj_limit;
    }

}