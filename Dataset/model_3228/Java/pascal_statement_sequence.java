





import java.util.List;
import java.util.ArrayList;

public class pascal_statement_sequence  {






    private List<pascal_statement> pascal_statements;




    private pascal_statement_part pascal_statement_part;


    public pascal_statement_sequence(
    ) {
        this.pascal_statements = new ArrayList<>();
    }

    public pascal_statement_sequence(
        ArrayList<pascal_statement> pascal_statements    ) {
        this.pascal_statements = pascal_statements;
    }


    public List<pascal_statement> getPascal_statements() {
        return pascal_statements;
    }

    public void addPascal_statement(Pascal_statement pascal_statement) {
        this.pascal_statements.add(pascal_statement);
    }
    public pascal_statement_part getPascal_statement_part() {
        return pascal_statement_part;
    }

    public void setPascal_statement_part(pascal_statement_part pascal_statement_part) {
        this.pascal_statement_part = pascal_statement_part;
    }

}