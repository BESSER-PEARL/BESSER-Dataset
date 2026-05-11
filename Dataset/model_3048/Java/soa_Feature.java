





import java.util.List;
import java.util.ArrayList;

public class soa_Feature  {

    private String name;





    private soa_Entity soa_entity;


    public soa_Feature(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public soa_Entity getSoa_entity() {
        return soa_entity;
    }

    public void setSoa_entity(soa_Entity soa_entity) {
        this.soa_entity = soa_entity;
    }

}