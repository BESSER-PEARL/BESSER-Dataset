





import java.util.List;
import java.util.ArrayList;

public class ulmDsl2_Feature  {

    private boolean mandatory;
    private boolean identifier;
    private String name;





    private ulmDsl2_Entity ulmdsl2_entity;


    public ulmDsl2_Feature(
        boolean mandatory,        boolean identifier,        String name    ) {
        this.mandatory = mandatory;
        this.identifier = identifier;
        this.name = name;
    }


    public boolean getMandatory() {
        return mandatory;
    }

    public void setMandatory(boolean mandatory) {
        this.mandatory = mandatory;
    }
    public boolean getIdentifier() {
        return identifier;
    }

    public void setIdentifier(boolean identifier) {
        this.identifier = identifier;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ulmDsl2_Entity getUlmdsl2_entity() {
        return ulmdsl2_entity;
    }

    public void setUlmdsl2_entity(ulmDsl2_Entity ulmdsl2_entity) {
        this.ulmdsl2_entity = ulmdsl2_entity;
    }

}