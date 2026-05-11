





import java.util.List;
import java.util.ArrayList;

public class myDot_Feature  {

    private String name;





    private myDot_Entity mydot_entity;


    public myDot_Feature(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public myDot_Entity getMydot_entity() {
        return mydot_entity;
    }

    public void setMydot_entity(myDot_Entity mydot_entity) {
        this.mydot_entity = mydot_entity;
    }

}