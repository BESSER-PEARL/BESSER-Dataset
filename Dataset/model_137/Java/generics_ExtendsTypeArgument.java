





import java.util.List;
import java.util.ArrayList;

public class generics_ExtendsTypeArgument extends TypeArgument {






    private List<TypeReference> typereferences;


    public generics_ExtendsTypeArgument(
    ) {
        super(
        );
        this.typereferences = new ArrayList<>();
    }

    public generics_ExtendsTypeArgument(
        ArrayList<TypeReference> typereferences    ) {
        this.typereferences = typereferences;
    }


    public List<TypeReference> getTypereferences() {
        return typereferences;
    }

    public void addTypereference(Typereference typereference) {
        this.typereferences.add(typereference);
    }

}