





import java.util.List;
import java.util.ArrayList;

public class metamodel_Model extends Type {






    private List<metamodel_Entity> metamodel_entitys;


    public metamodel_Model(
    ) {
        super(
        );
        this.metamodel_entitys = new ArrayList<>();
    }

    public metamodel_Model(
        ArrayList<metamodel_Entity> metamodel_entitys    ) {
        this.metamodel_entitys = metamodel_entitys;
    }


    public List<metamodel_Entity> getMetamodel_entitys() {
        return metamodel_entitys;
    }

    public void addMetamodel_entity(Metamodel_entity metamodel_entity) {
        this.metamodel_entitys.add(metamodel_entity);
    }

}