





import java.util.List;
import java.util.ArrayList;

public class cobol_tables_KeyName  {

    private String keyOrder;





    private List<IdentifierReference> identifierreferences;


    public cobol_tables_KeyName(
        String keyOrder    ) {
        this.keyOrder = keyOrder;
        this.identifierreferences = new ArrayList<>();
    }

    public cobol_tables_KeyName(
        String keyOrder        ArrayList<IdentifierReference> identifierreferences    ) {
        this.keyOrder = keyOrder;
        this.identifierreferences = identifierreferences;
    }

    public String getKeyorder() {
        return keyOrder;
    }

    public void setKeyorder(String keyOrder) {
        this.keyOrder = keyOrder;
    }

    public List<IdentifierReference> getIdentifierreferences() {
        return identifierreferences;
    }

    public void addIdentifierreference(Identifierreference identifierreference) {
        this.identifierreferences.add(identifierreference);
    }

}