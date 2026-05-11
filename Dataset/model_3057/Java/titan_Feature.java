





import java.util.List;
import java.util.ArrayList;

public class titan_Feature  {

    private String name;





    private titan_Entity titan_entity;


    public titan_Feature(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public titan_Entity getTitan_entity() {
        return titan_entity;
    }

    public void setTitan_entity(titan_Entity titan_entity) {
        this.titan_entity = titan_entity;
    }

}