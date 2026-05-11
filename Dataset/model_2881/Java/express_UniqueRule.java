





import java.util.List;
import java.util.ArrayList;

public class express_UniqueRule  {

    private String attribute;
    private String name;





    private express_Entity express_entity;


    public express_UniqueRule(
        String attribute,        String name    ) {
        this.attribute = attribute;
        this.name = name;
    }


    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public express_Entity getExpress_entity() {
        return express_entity;
    }

    public void setExpress_entity(express_Entity express_entity) {
        this.express_entity = express_entity;
    }

}