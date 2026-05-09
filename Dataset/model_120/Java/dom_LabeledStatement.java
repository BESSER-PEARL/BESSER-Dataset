





import java.util.List;
import java.util.ArrayList;

public class dom_LabeledStatement extends Statement {






    private dom_Statement dom_statement;




    private dom_Label dom_label;


    public dom_LabeledStatement(
    ) {
        super(
        );
    }



    public dom_Statement getDom_statement() {
        return dom_statement;
    }

    public void setDom_statement(dom_Statement dom_statement) {
        this.dom_statement = dom_statement;
    }
    public dom_Label getDom_label() {
        return dom_label;
    }

    public void setDom_label(dom_Label dom_label) {
        this.dom_label = dom_label;
    }

}