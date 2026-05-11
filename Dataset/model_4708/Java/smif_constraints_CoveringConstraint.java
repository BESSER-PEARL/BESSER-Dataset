





import java.util.List;
import java.util.ArrayList;

public class smif_constraints_CoveringConstraint extends TypeConstraint {






    private List<Type> types;


    public smif_constraints_CoveringConstraint(
    ) {
        super(
        );
        this.types = new ArrayList<>();
    }

    public smif_constraints_CoveringConstraint(
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