





import java.util.List;
import java.util.ArrayList;

public class titan_Reference extends Feature {

    private boolean unique;





    private titan_Entity titan_entity;


    public titan_Reference(
        boolean unique    ) {
        super(
        );
        this.unique = unique;
    }


    public boolean getUnique() {
        return unique;
    }

    public void setUnique(boolean unique) {
        this.unique = unique;
    }

    public titan_Entity getTitan_entity() {
        return titan_entity;
    }

    public void setTitan_entity(titan_Entity titan_entity) {
        this.titan_entity = titan_entity;
    }

}