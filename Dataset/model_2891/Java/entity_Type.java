





import java.util.List;
import java.util.ArrayList;

public class entity_Type  {

    private String name;





    private entity_Domain entity_domain;




    private entity_Feature entity_feature;


    public entity_Type(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public entity_Domain getEntity_domain() {
        return entity_domain;
    }

    public void setEntity_domain(entity_Domain entity_domain) {
        this.entity_domain = entity_domain;
    }
    public entity_Feature getEntity_feature() {
        return entity_feature;
    }

    public void setEntity_feature(entity_Feature entity_feature) {
        this.entity_feature = entity_feature;
    }

}