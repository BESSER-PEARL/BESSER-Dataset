





import java.util.List;
import java.util.ArrayList;

public class astm_gastm_TypeQualifiedIdentifierReference extends NameReference {






    private List<TypeReference> typereferences;


    public astm_gastm_TypeQualifiedIdentifierReference(
    ) {
        super(
        );
        this.typereferences = new ArrayList<>();
    }

    public astm_gastm_TypeQualifiedIdentifierReference(
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