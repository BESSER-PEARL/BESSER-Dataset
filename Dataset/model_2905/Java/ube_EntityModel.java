





import java.util.List;
import java.util.ArrayList;

public class ube_EntityModel  {






    private List<ube_Type> ube_types;


    public ube_EntityModel(
    ) {
        this.ube_types = new ArrayList<>();
    }

    public ube_EntityModel(
        ArrayList<ube_Type> ube_types    ) {
        this.ube_types = ube_types;
    }


    public List<ube_Type> getUbe_types() {
        return ube_types;
    }

    public void addUbe_type(Ube_type ube_type) {
        this.ube_types.add(ube_type);
    }

}