





import java.util.List;
import java.util.ArrayList;

public class cobol_statements_Initialize extends Statement {






    private List<Identifier> identifiers;


    public cobol_statements_Initialize(
    ) {
        super(
        );
        this.identifiers = new ArrayList<>();
    }

    public cobol_statements_Initialize(
        ArrayList<Identifier> identifiers    ) {
        this.identifiers = identifiers;
    }


    public List<Identifier> getIdentifiers() {
        return identifiers;
    }

    public void addIdentifier(Identifier identifier) {
        this.identifiers.add(identifier);
    }

}