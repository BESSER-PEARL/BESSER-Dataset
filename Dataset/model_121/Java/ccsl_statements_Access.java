





import java.util.List;
import java.util.ArrayList;

public class ccsl_statements_Access extends Statement {






    private statements_Statement statements_statement;




    private Element element;


    public ccsl_statements_Access(
    ) {
        super(
        );
    }



    public statements_Statement getStatements_statement() {
        return statements_statement;
    }

    public void setStatements_statement(statements_Statement statements_statement) {
        this.statements_statement = statements_statement;
    }
    public Element getElement() {
        return element;
    }

    public void setElement(Element element) {
        this.element = element;
    }

}