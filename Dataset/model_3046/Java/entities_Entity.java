





import java.util.List;
import java.util.ArrayList;

public class entities_Entity  {

    private String name;





    private entities_DomainModel entities_domainmodel;




    private entities_Entity entities_entity;


    public entities_Entity(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public entities_DomainModel getEntities_domainmodel() {
        return entities_domainmodel;
    }

    public void setEntities_domainmodel(entities_DomainModel entities_domainmodel) {
        this.entities_domainmodel = entities_domainmodel;
    }
    public entities_Entity getEntities_entity() {
        return entities_entity;
    }

    public void setEntities_entity(entities_Entity entities_entity) {
        this.entities_entity = entities_entity;
    }

}