





import java.util.List;
import java.util.ArrayList;

public class dom_Source extends Node {






    private List<dom_Statement> dom_statements;


    public dom_Source(
    ) {
        super(
        );
        this.dom_statements = new ArrayList<>();
    }

    public dom_Source(
        ArrayList<dom_Statement> dom_statements    ) {
        this.dom_statements = dom_statements;
    }


    public List<dom_Statement> getDom_statements() {
        return dom_statements;
    }

    public void addDom_statement(Dom_statement dom_statement) {
        this.dom_statements.add(dom_statement);
    }

}