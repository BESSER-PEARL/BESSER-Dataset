





import java.util.List;
import java.util.ArrayList;

public class swml_Attribute  {

    private String Typ;
    private String name;





    private swml_Entity swml_entity;


    public swml_Attribute(
        String Typ,        String name    ) {
        this.Typ = Typ;
        this.name = name;
    }


    public String getTyp() {
        return Typ;
    }

    public void setTyp(String Typ) {
        this.Typ = Typ;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public swml_Entity getSwml_entity() {
        return swml_entity;
    }

    public void setSwml_entity(swml_Entity swml_entity) {
        this.swml_entity = swml_entity;
    }

}