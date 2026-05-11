





import java.util.List;
import java.util.ArrayList;

public class pascal_with_statement  {






    private List<pascal_variable> pascal_variables;




    private pascal_statement pascal_statement;




    private pascal_structured_statement pascal_structured_statement;


    public pascal_with_statement(
    ) {
        this.pascal_variables = new ArrayList<>();
    }

    public pascal_with_statement(
        ArrayList<pascal_variable> pascal_variables    ) {
        this.pascal_variables = pascal_variables;
    }


    public List<pascal_variable> getPascal_variables() {
        return pascal_variables;
    }

    public void addPascal_variable(Pascal_variable pascal_variable) {
        this.pascal_variables.add(pascal_variable);
    }
    public pascal_statement getPascal_statement() {
        return pascal_statement;
    }

    public void setPascal_statement(pascal_statement pascal_statement) {
        this.pascal_statement = pascal_statement;
    }
    public pascal_structured_statement getPascal_structured_statement() {
        return pascal_structured_statement;
    }

    public void setPascal_structured_statement(pascal_structured_statement pascal_structured_statement) {
        this.pascal_structured_statement = pascal_structured_statement;
    }

}