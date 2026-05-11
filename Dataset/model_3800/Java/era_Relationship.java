





import java.util.List;
import java.util.ArrayList;

public class era_Relationship  {

    private String name;





    private List<era_Entity> era_entitys;




    private era_Entity era_entity;


    public era_Relationship(
        String name    ) {
        this.name = name;
        this.era_entitys = new ArrayList<>();
    }

    public era_Relationship(
        String name        ArrayList<era_Entity> era_entitys    ) {
        this.name = name;
        this.era_entitys = era_entitys;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<era_Entity> getEra_entitys() {
        return era_entitys;
    }

    public void addEra_entity(Era_entity era_entity) {
        this.era_entitys.add(era_entity);
    }
    public era_Entity getEra_entity() {
        return era_entity;
    }

    public void setEra_entity(era_Entity era_entity) {
        this.era_entity = era_entity;
    }

}