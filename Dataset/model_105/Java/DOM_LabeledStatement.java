





import java.util.List;
import java.util.ArrayList;

public class DOM_LabeledStatement extends Statement {






    private DOM_Statement dom_statement;




    private DOM_SimpleName dom_simplename;


    public DOM_LabeledStatement(
    ) {
        super(
        );
    }



    public DOM_Statement getDom_statement() {
        return dom_statement;
    }

    public void setDom_statement(DOM_Statement dom_statement) {
        this.dom_statement = dom_statement;
    }
    public DOM_SimpleName getDom_simplename() {
        return dom_simplename;
    }

    public void setDom_simplename(DOM_SimpleName dom_simplename) {
        this.dom_simplename = dom_simplename;
    }

}