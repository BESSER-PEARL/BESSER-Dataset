





import java.util.List;
import java.util.ArrayList;

public class domainmodel_Feature  {

    private boolean required;
    private String name;
    private boolean many;





    private domainmodel_Type domainmodel_type;




    private domainmodel_Entity domainmodel_entity;


    public domainmodel_Feature(
        boolean required,        String name,        boolean many    ) {
        this.required = required;
        this.name = name;
        this.many = many;
    }


    public boolean getRequired() {
        return required;
    }

    public void setRequired(boolean required) {
        this.required = required;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getMany() {
        return many;
    }

    public void setMany(boolean many) {
        this.many = many;
    }

    public domainmodel_Type getDomainmodel_type() {
        return domainmodel_type;
    }

    public void setDomainmodel_type(domainmodel_Type domainmodel_type) {
        this.domainmodel_type = domainmodel_type;
    }
    public domainmodel_Entity getDomainmodel_entity() {
        return domainmodel_entity;
    }

    public void setDomainmodel_entity(domainmodel_Entity domainmodel_entity) {
        this.domainmodel_entity = domainmodel_entity;
    }

}