





import java.util.List;
import java.util.ArrayList;

public class astm_TypeQualifiedIdentifierReference extends NameReference {






    private List<astm_TypeReference> astm_typereferences;




    private astm_IdentifierReference astm_identifierreference;


    public astm_TypeQualifiedIdentifierReference(
    ) {
        super(
        );
        this.astm_typereferences = new ArrayList<>();
    }

    public astm_TypeQualifiedIdentifierReference(
        ArrayList<astm_TypeReference> astm_typereferences    ) {
        this.astm_typereferences = astm_typereferences;
    }


    public List<astm_TypeReference> getAstm_typereferences() {
        return astm_typereferences;
    }

    public void addAstm_typereference(Astm_typereference astm_typereference) {
        this.astm_typereferences.add(astm_typereference);
    }
    public astm_IdentifierReference getAstm_identifierreference() {
        return astm_identifierreference;
    }

    public void setAstm_identifierreference(astm_IdentifierReference astm_identifierreference) {
        this.astm_identifierreference = astm_identifierreference;
    }

}