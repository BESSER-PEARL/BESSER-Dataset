





import java.util.List;
import java.util.ArrayList;

public class dom_SelectProperties extends SelectStatement {

    private boolean distinct;





    private List<dom_Expression> dom_expressions;


    public dom_SelectProperties(
        boolean distinct    ) {
        super(
        );
        this.distinct = distinct;
        this.dom_expressions = new ArrayList<>();
    }

    public dom_SelectProperties(
        boolean distinct        ArrayList<dom_Expression> dom_expressions    ) {
        this.distinct = distinct;
        this.dom_expressions = dom_expressions;
    }

    public boolean getDistinct() {
        return distinct;
    }

    public void setDistinct(boolean distinct) {
        this.distinct = distinct;
    }

    public List<dom_Expression> getDom_expressions() {
        return dom_expressions;
    }

    public void addDom_expression(Dom_expression dom_expression) {
        this.dom_expressions.add(dom_expression);
    }

}