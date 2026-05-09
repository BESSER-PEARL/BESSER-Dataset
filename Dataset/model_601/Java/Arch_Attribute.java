





import java.util.List;
import java.util.ArrayList;

public class Arch_Attribute  {

    private String type;
    private String name;





    private Arch_Entity arch_entity;


    public Arch_Attribute(
        String type,        String name    ) {
        this.type = type;
        this.name = name;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Arch_Entity getArch_entity() {
        return arch_entity;
    }

    public void setArch_entity(Arch_Entity arch_entity) {
        this.arch_entity = arch_entity;
    }

}