





import java.util.List;
import java.util.ArrayList;

public class domainmodel_Feature  {

    private String value;
    private boolean many;
    private String name;





    private domainmodel_Entity domainmodel_entity;


    public domainmodel_Feature(
        String value,        boolean many,        String name    ) {
        this.value = value;
        this.many = many;
        this.name = name;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public boolean getMany() {
        return many;
    }

    public void setMany(boolean many) {
        this.many = many;
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