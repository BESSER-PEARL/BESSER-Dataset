





import java.util.List;
import java.util.ArrayList;

public class domainmodel_Feature  {

    private String s;
    private boolean many;
    private String type;
    private String name;





    private domainmodel_Entity domainmodel_entity;


    public domainmodel_Feature(
        String s,        boolean many,        String type,        String name    ) {
        this.s = s;
        this.many = many;
        this.type = type;
        this.name = name;
    }


    public String getS() {
        return s;
    }

    public void setS(String s) {
        this.s = s;
    }
    public boolean getMany() {
        return many;
    }

    public void setMany(boolean many) {
        this.many = many;
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

    public domainmodel_Entity getDomainmodel_entity() {
        return domainmodel_entity;
    }

    public void setDomainmodel_entity(domainmodel_Entity domainmodel_entity) {
        this.domainmodel_entity = domainmodel_entity;
    }

}