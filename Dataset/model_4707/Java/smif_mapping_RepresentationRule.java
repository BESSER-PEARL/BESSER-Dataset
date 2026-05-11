





import java.util.List;
import java.util.ArrayList;

public class smif_mapping_RepresentationRule extends ConditionalRule {

    private String mapAll;





    private List<Type> types;




    private Type type;


    public smif_mapping_RepresentationRule(
        String mapAll    ) {
        super(
        );
        this.mapAll = mapAll;
        this.types = new ArrayList<>();
    }

    public smif_mapping_RepresentationRule(
        String mapAll        ArrayList<Type> types    ) {
        this.mapAll = mapAll;
        this.types = types;
    }

    public String getMapall() {
        return mapAll;
    }

    public void setMapall(String mapAll) {
        this.mapAll = mapAll;
    }

    public List<Type> getTypes() {
        return types;
    }

    public void addType(Type type) {
        this.types.add(type);
    }
    public Type getType() {
        return type;
    }

    public void setType(Type type) {
        this.type = type;
    }

}