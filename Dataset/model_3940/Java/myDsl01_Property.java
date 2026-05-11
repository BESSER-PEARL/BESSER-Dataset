





import java.util.List;
import java.util.ArrayList;

public class myDsl01_Property  {

    private String name;





    private myDsl01_Entity mydsl01_entity;


    public myDsl01_Property(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public myDsl01_Entity getMydsl01_entity() {
        return mydsl01_entity;
    }

    public void setMydsl01_entity(myDsl01_Entity mydsl01_entity) {
        this.mydsl01_entity = mydsl01_entity;
    }

}