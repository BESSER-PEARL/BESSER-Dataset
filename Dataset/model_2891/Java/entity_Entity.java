





import java.util.List;
import java.util.ArrayList;

public class entity_Entity extends Type {






    private List<entity_Feature> entity_features;


    public entity_Entity(
    ) {
        super(
        );
        this.entity_features = new ArrayList<>();
    }

    public entity_Entity(
        ArrayList<entity_Feature> entity_features    ) {
        this.entity_features = entity_features;
    }


    public List<entity_Feature> getEntity_features() {
        return entity_features;
    }

    public void addEntity_feature(Entity_feature entity_feature) {
        this.entity_features.add(entity_feature);
    }

}