





import java.util.List;
import java.util.ArrayList;

public class ulmDsl2_Entity  {

    private String name;
    private String desc;
    private String type;





    private ulmDsl2_Entity ulmdsl2_entity;


    public ulmDsl2_Entity(
        String name,        String desc,        String type    ) {
        this.name = name;
        this.desc = desc;
        this.type = type;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDesc() {
        return desc;
    }

    public void setDesc(String desc) {
        this.desc = desc;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public ulmDsl2_Entity getUlmdsl2_entity() {
        return ulmdsl2_entity;
    }

    public void setUlmdsl2_entity(ulmDsl2_Entity ulmdsl2_entity) {
        this.ulmdsl2_entity = ulmdsl2_entity;
    }

}