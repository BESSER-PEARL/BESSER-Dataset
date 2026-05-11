





import java.util.List;
import java.util.ArrayList;

public class modelDsl_Relation  {

    private String name;
    private String multiplicity;
    private String navigable;





    private modelDsl_SimpleLink modeldsl_simplelink;




    private modelDsl_Entity modeldsl_entity;




    private modelDsl_AssociativeEntity modeldsl_associativeentity;


    public modelDsl_Relation(
        String name,        String multiplicity,        String navigable    ) {
        this.name = name;
        this.multiplicity = multiplicity;
        this.navigable = navigable;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getMultiplicity() {
        return multiplicity;
    }

    public void setMultiplicity(String multiplicity) {
        this.multiplicity = multiplicity;
    }
    public String getNavigable() {
        return navigable;
    }

    public void setNavigable(String navigable) {
        this.navigable = navigable;
    }

    public modelDsl_SimpleLink getModeldsl_simplelink() {
        return modeldsl_simplelink;
    }

    public void setModeldsl_simplelink(modelDsl_SimpleLink modeldsl_simplelink) {
        this.modeldsl_simplelink = modeldsl_simplelink;
    }
    public modelDsl_Entity getModeldsl_entity() {
        return modeldsl_entity;
    }

    public void setModeldsl_entity(modelDsl_Entity modeldsl_entity) {
        this.modeldsl_entity = modeldsl_entity;
    }
    public modelDsl_AssociativeEntity getModeldsl_associativeentity() {
        return modeldsl_associativeentity;
    }

    public void setModeldsl_associativeentity(modelDsl_AssociativeEntity modeldsl_associativeentity) {
        this.modeldsl_associativeentity = modeldsl_associativeentity;
    }

}