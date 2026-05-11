





import java.util.List;
import java.util.ArrayList;

public class dom_TransactionStatement extends Statement {






    private dom_Block dom_block;




    private List<dom_NameExpression> dom_nameexpressions;


    public dom_TransactionStatement(
    ) {
        super(
        );
        this.dom_nameexpressions = new ArrayList<>();
    }

    public dom_TransactionStatement(
        ArrayList<dom_NameExpression> dom_nameexpressions    ) {
        this.dom_nameexpressions = dom_nameexpressions;
    }


    public dom_Block getDom_block() {
        return dom_block;
    }

    public void setDom_block(dom_Block dom_block) {
        this.dom_block = dom_block;
    }
    public List<dom_NameExpression> getDom_nameexpressions() {
        return dom_nameexpressions;
    }

    public void addDom_nameexpression(Dom_nameexpression dom_nameexpression) {
        this.dom_nameexpressions.add(dom_nameexpression);
    }

}