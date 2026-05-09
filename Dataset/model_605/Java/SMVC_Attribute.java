





import java.util.List;
import java.util.ArrayList;

public class SMVC_Attribute  {

    private boolean multiValued;
    private String name;
    private String type;





    private SMVC_Entity smvc_entity;




    private SMVC_Entity smvc_entity;


    public SMVC_Attribute(
        boolean multiValued,        String name,        String type    ) {
        this.multiValued = multiValued;
        this.name = name;
        this.type = type;
    }


    public boolean getMultivalued() {
        return multiValued;
    }

    public void setMultivalued(boolean multiValued) {
        this.multiValued = multiValued;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public SMVC_Entity getSmvc_entity() {
        return smvc_entity;
    }

    public void setSmvc_entity(SMVC_Entity smvc_entity) {
        this.smvc_entity = smvc_entity;
    }
    public SMVC_Entity getSmvc_entity() {
        return smvc_entity;
    }

    public void setSmvc_entity(SMVC_Entity smvc_entity) {
        this.smvc_entity = smvc_entity;
    }

}