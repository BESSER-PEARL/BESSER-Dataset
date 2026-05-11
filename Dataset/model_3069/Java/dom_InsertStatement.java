





import java.util.List;
import java.util.ArrayList;

public class dom_InsertStatement extends QlStatement {






    private dom_Entity dom_entity;




    private List<dom_Expression> dom_expressions;


    public dom_InsertStatement(
    ) {
        super(
        );
        this.dom_expressions = new ArrayList<>();
    }

    public dom_InsertStatement(
        ArrayList<dom_Expression> dom_expressions    ) {
        this.dom_expressions = dom_expressions;
    }


    public dom_Entity getDom_entity() {
        return dom_entity;
    }

    public void setDom_entity(dom_Entity dom_entity) {
        this.dom_entity = dom_entity;
    }
    public List<dom_Expression> getDom_expressions() {
        return dom_expressions;
    }

    public void addDom_expression(Dom_expression dom_expression) {
        this.dom_expressions.add(dom_expression);
    }

}