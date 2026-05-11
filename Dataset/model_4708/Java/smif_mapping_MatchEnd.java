





import java.util.List;
import java.util.ArrayList;

public class smif_mapping_MatchEnd extends constraints_Conditional, patterns_Computed {






    private List<Type> types;


    public smif_mapping_MatchEnd(
    ) {
        super(
        );
        this.types = new ArrayList<>();
    }

    public smif_mapping_MatchEnd(
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