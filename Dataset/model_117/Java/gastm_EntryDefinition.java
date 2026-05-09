





import java.util.List;
import java.util.ArrayList;

public class gastm_EntryDefinition extends Definition {






    private List<gastm_Statement> gastm_statements;


    public gastm_EntryDefinition(
    ) {
        super(
        );
        this.gastm_statements = new ArrayList<>();
    }

    public gastm_EntryDefinition(
        ArrayList<gastm_Statement> gastm_statements    ) {
        this.gastm_statements = gastm_statements;
    }


    public List<gastm_Statement> getGastm_statements() {
        return gastm_statements;
    }

    public void addGastm_statement(Gastm_statement gastm_statement) {
        this.gastm_statements.add(gastm_statement);
    }

}