





import java.util.List;
import java.util.ArrayList;

public class metamodel_idFeature extends Feature {

    private String generationType;





    private metamodel_Entity metamodel_entity;


    public metamodel_idFeature(
        String generationType    ) {
        super(
        );
        this.generationType = generationType;
    }


    public String getGenerationtype() {
        return generationType;
    }

    public void setGenerationtype(String generationType) {
        this.generationType = generationType;
    }

    public metamodel_Entity getMetamodel_entity() {
        return metamodel_entity;
    }

    public void setMetamodel_entity(metamodel_Entity metamodel_entity) {
        this.metamodel_entity = metamodel_entity;
    }

}