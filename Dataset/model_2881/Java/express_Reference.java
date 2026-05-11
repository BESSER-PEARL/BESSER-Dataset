





import java.util.List;
import java.util.ArrayList;

public class express_Reference  {

    private String name;
    private boolean optional;
    private boolean self;
    private String qualifier;





    private express_Entity express_entity;


    public express_Reference(
        String name,        boolean optional,        boolean self,        String qualifier    ) {
        this.name = name;
        this.optional = optional;
        this.self = self;
        this.qualifier = qualifier;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getOptional() {
        return optional;
    }

    public void setOptional(boolean optional) {
        this.optional = optional;
    }
    public boolean getSelf() {
        return self;
    }

    public void setSelf(boolean self) {
        this.self = self;
    }
    public String getQualifier() {
        return qualifier;
    }

    public void setQualifier(String qualifier) {
        this.qualifier = qualifier;
    }

    public express_Entity getExpress_entity() {
        return express_entity;
    }

    public void setExpress_entity(express_Entity express_entity) {
        this.express_entity = express_entity;
    }

}