





import java.util.List;
import java.util.ArrayList;

public class swml_EnumTyp  {

    private String name;





    private swml_Enumeration swml_enumeration;




    private swml_Entity swml_entity;


    public swml_EnumTyp(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public swml_Enumeration getSwml_enumeration() {
        return swml_enumeration;
    }

    public void setSwml_enumeration(swml_Enumeration swml_enumeration) {
        this.swml_enumeration = swml_enumeration;
    }
    public swml_Entity getSwml_entity() {
        return swml_entity;
    }

    public void setSwml_entity(swml_Entity swml_entity) {
        this.swml_entity = swml_entity;
    }

}