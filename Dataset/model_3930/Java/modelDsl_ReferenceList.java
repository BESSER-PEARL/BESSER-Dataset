





import java.util.List;
import java.util.ArrayList;

public class modelDsl_ReferenceList extends Field {






    private modelDsl_Entity modeldsl_entity;




    private modelDsl_EntityElements modeldsl_entityelements;




    private modelDsl_Reference modeldsl_reference;


    public modelDsl_ReferenceList(
    ) {
        super(
        );
    }



    public modelDsl_Entity getModeldsl_entity() {
        return modeldsl_entity;
    }

    public void setModeldsl_entity(modelDsl_Entity modeldsl_entity) {
        this.modeldsl_entity = modeldsl_entity;
    }
    public modelDsl_EntityElements getModeldsl_entityelements() {
        return modeldsl_entityelements;
    }

    public void setModeldsl_entityelements(modelDsl_EntityElements modeldsl_entityelements) {
        this.modeldsl_entityelements = modeldsl_entityelements;
    }
    public modelDsl_Reference getModeldsl_reference() {
        return modeldsl_reference;
    }

    public void setModeldsl_reference(modelDsl_Reference modeldsl_reference) {
        this.modeldsl_reference = modeldsl_reference;
    }

}