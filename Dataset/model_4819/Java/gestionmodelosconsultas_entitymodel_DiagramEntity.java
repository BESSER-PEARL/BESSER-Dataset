





import java.util.List;
import java.util.ArrayList;

public class gestionmodelosconsultas_entitymodel_DiagramEntity  {






    private List<Entity> entitys;


    public gestionmodelosconsultas_entitymodel_DiagramEntity(
    ) {
        this.entitys = new ArrayList<>();
    }

    public gestionmodelosconsultas_entitymodel_DiagramEntity(
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