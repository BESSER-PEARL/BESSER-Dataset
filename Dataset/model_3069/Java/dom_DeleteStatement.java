





import java.util.List;
import java.util.ArrayList;

public class dom_DeleteStatement extends QlStatement {

    private String name;





    private dom_Expression dom_expression;




    private dom_Entity dom_entity;


    public dom_DeleteStatement(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public dom_Expression getDom_expression() {
        return dom_expression;
    }

    public void setDom_expression(dom_Expression dom_expression) {
        this.dom_expression = dom_expression;
    }
    public dom_Entity getDom_entity() {
        return dom_entity;
    }

    public void setDom_entity(dom_Entity dom_entity) {
        this.dom_entity = dom_entity;
    }

}