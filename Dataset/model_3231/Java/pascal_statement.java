





import java.util.List;
import java.util.ArrayList;

public class pascal_statement  {






    private pascal_simple_statement pascal_simple_statement;




    private pascal_with_statement pascal_with_statement;




    private pascal_label pascal_label;




    private pascal_structured_statement pascal_structured_statement;




    private pascal_statement_sequence pascal_statement_sequence;


    public pascal_statement(
    ) {
    }



    public pascal_simple_statement getPascal_simple_statement() {
        return pascal_simple_statement;
    }

    public void setPascal_simple_statement(pascal_simple_statement pascal_simple_statement) {
        this.pascal_simple_statement = pascal_simple_statement;
    }
    public pascal_with_statement getPascal_with_statement() {
        return pascal_with_statement;
    }

    public void setPascal_with_statement(pascal_with_statement pascal_with_statement) {
        this.pascal_with_statement = pascal_with_statement;
    }
    public pascal_label getPascal_label() {
        return pascal_label;
    }

    public void setPascal_label(pascal_label pascal_label) {
        this.pascal_label = pascal_label;
    }
    public pascal_structured_statement getPascal_structured_statement() {
        return pascal_structured_statement;
    }

    public void setPascal_structured_statement(pascal_structured_statement pascal_structured_statement) {
        this.pascal_structured_statement = pascal_structured_statement;
    }
    public pascal_statement_sequence getPascal_statement_sequence() {
        return pascal_statement_sequence;
    }

    public void setPascal_statement_sequence(pascal_statement_sequence pascal_statement_sequence) {
        this.pascal_statement_sequence = pascal_statement_sequence;
    }

}