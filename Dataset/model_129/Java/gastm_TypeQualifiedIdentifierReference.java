





import java.util.List;
import java.util.ArrayList;

public class gastm_TypeQualifiedIdentifierReference extends NameReference {






    private IdentifierReference identifierreference;




    private List<TypeReference> typereferences;


    public gastm_TypeQualifiedIdentifierReference(
    ) {
        super(
        );
        this.typereferences = new ArrayList<>();
    }

    public gastm_TypeQualifiedIdentifierReference(
        ArrayList<TypeReference> typereferences    ) {
        this.typereferences = typereferences;
    }


    public IdentifierReference getIdentifierreference() {
        return identifierreference;
    }

    public void setIdentifierreference(IdentifierReference identifierreference) {
        this.identifierreference = identifierreference;
    }
    public List<TypeReference> getTypereferences() {
        return typereferences;
    }

    public void addTypereference(Typereference typereference) {
        this.typereferences.add(typereference);
    }

}