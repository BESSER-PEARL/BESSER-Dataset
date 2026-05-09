





import java.util.List;
import java.util.ArrayList;

public class astm_TypeQualifiedIdentifierReference extends NameReference {






    private List<TypeReference> typereferences;


    public astm_TypeQualifiedIdentifierReference(
    ) {
        super(
        );
        this.typereferences = new ArrayList<>();
    }

    public astm_TypeQualifiedIdentifierReference(
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