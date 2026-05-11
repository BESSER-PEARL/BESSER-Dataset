





import java.util.List;
import java.util.ArrayList;

public class cobol_identifiers_IdentifierReference extends references_Qualifiable, identifiers_Identifier, references_ElementReference {






    private List<Qualifier> qualifiers;


    public cobol_identifiers_IdentifierReference(
    ) {
        super(
        );
        this.qualifiers = new ArrayList<>();
    }

    public cobol_identifiers_IdentifierReference(
        ArrayList<Qualifier> qualifiers    ) {
        this.qualifiers = qualifiers;
    }


    public List<Qualifier> getQualifiers() {
        return qualifiers;
    }

    public void addQualifier(Qualifier qualifier) {
        this.qualifiers.add(qualifier);
    }

}