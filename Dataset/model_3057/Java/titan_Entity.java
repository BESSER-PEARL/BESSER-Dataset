





import java.util.List;
import java.util.ArrayList;

public class titan_Entity  {

    private String name;





    private titan_Entity titan_entity;




    private titan_Package titan_package;


    public titan_Entity(
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
    public titan_Package getTitan_package() {
        return titan_package;
    }

    public void setTitan_package(titan_Package titan_package) {
        this.titan_package = titan_package;
    }

}