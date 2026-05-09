





import java.util.List;
import java.util.ArrayList;

public class eTJ_Alternative extends AllocateResourceAttribute {






    private List<eTJ_Resource> etj_resources;


    public eTJ_Alternative(
    ) {
        super(
        );
        this.etj_resources = new ArrayList<>();
    }

    public eTJ_Alternative(
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