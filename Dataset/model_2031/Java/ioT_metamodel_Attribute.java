





import java.util.List;
import java.util.ArrayList;

public class ioT_metamodel_Attribute extends Entity {

    private String name;
    private String Type;



    public ioT_metamodel_Attribute(
        String name,        String Type    ) {
        super(
        );
        this.name = name;
        this.Type = Type;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return Type;
    }

    public void setType(String Type) {
        this.Type = Type;
    }


}