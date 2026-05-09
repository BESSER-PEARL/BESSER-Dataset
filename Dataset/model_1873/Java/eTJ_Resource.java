





import java.util.List;
import java.util.ArrayList;

public class eTJ_Resource extends ResourceAttribute, Property {

    private String id;
    private String name;





    private eTJ_SupplementResource etj_supplementresource;




    private eTJ_StatusSheet etj_statussheet;


    public eTJ_Resource(
        String id,        String name    ) {
        super(
        );
        this.id = id;
        this.name = name;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public eTJ_SupplementResource getEtj_supplementresource() {
        return etj_supplementresource;
    }

    public void setEtj_supplementresource(eTJ_SupplementResource etj_supplementresource) {
        this.etj_supplementresource = etj_supplementresource;
    }
    public eTJ_StatusSheet getEtj_statussheet() {
        return etj_statussheet;
    }

    public void setEtj_statussheet(eTJ_StatusSheet etj_statussheet) {
        this.etj_statussheet = etj_statussheet;
    }

}