





import java.util.List;
import java.util.ArrayList;

public class myDsl_Property  {

    private String name;





    private myDsl_Type mydsl_type;




    private myDsl_Entity mydsl_entity;


    public myDsl_Property(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public myDsl_Type getMydsl_type() {
        return mydsl_type;
    }

    public void setMydsl_type(myDsl_Type mydsl_type) {
        this.mydsl_type = mydsl_type;
    }
    public myDsl_Entity getMydsl_entity() {
        return mydsl_entity;
    }

    public void setMydsl_entity(myDsl_Entity mydsl_entity) {
        this.mydsl_entity = mydsl_entity;
    }

}