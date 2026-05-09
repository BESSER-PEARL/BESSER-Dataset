





import java.util.List;
import java.util.ArrayList;

public class model_datasources_QueryMatchingCriteria  {






    private List<Type> types;


    public model_datasources_QueryMatchingCriteria(
    ) {
        this.types = new ArrayList<>();
    }

    public model_datasources_QueryMatchingCriteria(
        ArrayList<Type> types    ) {
        this.types = types;
    }


    public List<Type> getTypes() {
        return types;
    }

    public void addType(Type type) {
        this.types.add(type);
    }

}