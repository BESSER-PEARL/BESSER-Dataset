





import java.util.List;
import java.util.ArrayList;

public class domainModel_Feature  {

    private String name;
    private boolean many;





    private domainModel_Entity domainmodel_entity;




    private domainModel_Type domainmodel_type;


    public domainModel_Feature(
        String name,        boolean many    ) {
        this.name = name;
        this.many = many;
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

    public domainModel_Entity getDomainmodel_entity() {
        return domainmodel_entity;
    }

    public void setDomainmodel_entity(domainModel_Entity domainmodel_entity) {
        this.domainmodel_entity = domainmodel_entity;
    }
    public domainModel_Type getDomainmodel_type() {
        return domainmodel_type;
    }

    public void setDomainmodel_type(domainModel_Type domainmodel_type) {
        this.domainmodel_type = domainmodel_type;
    }

}