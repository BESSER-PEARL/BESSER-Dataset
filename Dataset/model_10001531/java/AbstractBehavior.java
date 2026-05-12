





import java.util.List;
import java.util.ArrayList;

public class AbstractBehavior  {






    private List<Entity> entitys;


    public AbstractBehavior(
    ) {
        this.entitys = new ArrayList<>();
    }

    public AbstractBehavior(
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