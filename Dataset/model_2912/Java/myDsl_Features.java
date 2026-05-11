





import java.util.List;
import java.util.ArrayList;

public class myDsl_Features  {

    private String name;





    private myDsl_Entity mydsl_entity;




    private myDsl_Type mydsl_type;


    public myDsl_Features(
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
    public myDsl_Type getMydsl_type() {
        return mydsl_type;
    }

    public void setMydsl_type(myDsl_Type mydsl_type) {
        this.mydsl_type = mydsl_type;
    }

}