





import java.util.List;
import java.util.ArrayList;

public class entities_Model  {






    private List<entities_Entity> entities_entitys;


    public entities_Model(
    ) {
        this.entities_entitys = new ArrayList<>();
    }

    public entities_Model(
        ArrayList<entities_Entity> entities_entitys    ) {
        this.entities_entitys = entities_entitys;
    }


    public List<entities_Entity> getEntities_entitys() {
        return entities_entitys;
    }

    public void addEntities_entity(Entities_entity entities_entity) {
        this.entities_entitys.add(entities_entity);
    }

}