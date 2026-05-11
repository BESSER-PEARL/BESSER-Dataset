





import java.util.List;
import java.util.ArrayList;

public class soa_Entities  {

    private String name;





    private soa_Model soa_model;




    private soa_EntitiesFeature soa_entitiesfeature;


    public soa_Entities(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public soa_Model getSoa_model() {
        return soa_model;
    }

    public void setSoa_model(soa_Model soa_model) {
        this.soa_model = soa_model;
    }
    public soa_EntitiesFeature getSoa_entitiesfeature() {
        return soa_entitiesfeature;
    }

    public void setSoa_entitiesfeature(soa_EntitiesFeature soa_entitiesfeature) {
        this.soa_entitiesfeature = soa_entitiesfeature;
    }

}