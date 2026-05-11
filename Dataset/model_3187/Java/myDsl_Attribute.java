





import java.util.List;
import java.util.ArrayList;

public class myDsl_Attribute  {

    private String name;





    private myDsl_Entity mydsl_entity;


    public myDsl_Attribute(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public myDsl_Entity getMydsl_entity() {
        return mydsl_entity;
    }

    public void setMydsl_entity(myDsl_Entity mydsl_entity) {
        this.mydsl_entity = mydsl_entity;
    }

}