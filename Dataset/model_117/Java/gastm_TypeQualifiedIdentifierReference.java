





import java.util.List;
import java.util.ArrayList;

public class gastm_TypeQualifiedIdentifierReference extends NameReference {






    private List<gastm_TypeReference> gastm_typereferences;




    private gastm_IdentifierReference gastm_identifierreference;


    public gastm_TypeQualifiedIdentifierReference(
    ) {
        super(
        );
        this.gastm_typereferences = new ArrayList<>();
    }

    public gastm_TypeQualifiedIdentifierReference(
        ArrayList<gastm_TypeReference> gastm_typereferences    ) {
        this.gastm_typereferences = gastm_typereferences;
    }


    public List<gastm_TypeReference> getGastm_typereferences() {
        return gastm_typereferences;
    }

    public void addGastm_typereference(Gastm_typereference gastm_typereference) {
        this.gastm_typereferences.add(gastm_typereference);
    }
    public gastm_IdentifierReference getGastm_identifierreference() {
        return gastm_identifierreference;
    }

    public void setGastm_identifierreference(gastm_IdentifierReference gastm_identifierreference) {
        this.gastm_identifierreference = gastm_identifierreference;
    }

}