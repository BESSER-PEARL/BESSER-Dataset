





import java.util.List;
import java.util.ArrayList;

public class forms_entityModeling_List extends RelationshipPageElement {






    private List<Entity> entitys;


    public forms_entityModeling_List(
    ) {
        super(
        );
        this.entitys = new ArrayList<>();
    }

    public forms_entityModeling_List(
        ArrayList<Entity> entitys    ) {
        this.entitys = entitys;
    }


    public List<Entity> getEntitys() {
        return entitys;
    }

    public void addEntity(Entity entity) {
        this.entitys.add(entity);
    }

}