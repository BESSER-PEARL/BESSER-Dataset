





import java.util.List;
import java.util.ArrayList;

public class modelDsl_Reference extends Field {

    private boolean optional;





    private modelDsl_EntityElements modeldsl_entityelements;




    private modelDsl_Entity modeldsl_entity;


    public modelDsl_Reference(
        boolean optional    ) {
        super(
        );
        this.optional = optional;
    }


    public boolean getOptional() {
        return optional;
    }

    public void setOptional(boolean optional) {
        this.optional = optional;
    }

    public modelDsl_EntityElements getModeldsl_entityelements() {
        return modeldsl_entityelements;
    }

    public void setModeldsl_entityelements(modelDsl_EntityElements modeldsl_entityelements) {
        this.modeldsl_entityelements = modeldsl_entityelements;
    }
    public modelDsl_Entity getModeldsl_entity() {
        return modeldsl_entity;
    }

    public void setModeldsl_entity(modelDsl_Entity modeldsl_entity) {
        this.modeldsl_entity = modeldsl_entity;
    }

}