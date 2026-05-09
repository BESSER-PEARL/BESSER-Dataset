





import java.util.List;
import java.util.ArrayList;

public class FlatQVT_Operation extends TypedElement, MultiplicityElement {






    private List<Type> types;


    public FlatQVT_Operation(
    ) {
        super(
        );
        this.types = new ArrayList<>();
    }

    public FlatQVT_Operation(
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