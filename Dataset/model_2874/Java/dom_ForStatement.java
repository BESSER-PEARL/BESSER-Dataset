





import java.util.List;
import java.util.ArrayList;

public class dom_ForStatement extends Statement {






    private dom_FormalParameterExpression dom_formalparameterexpression;




    private dom_Block dom_block;




    private dom_Expression dom_expression;


    public dom_ForStatement(
    ) {
        super(
        );
    }



    public dom_FormalParameterExpression getDom_formalparameterexpression() {
        return dom_formalparameterexpression;
    }

    public void setDom_formalparameterexpression(dom_FormalParameterExpression dom_formalparameterexpression) {
        this.dom_formalparameterexpression = dom_formalparameterexpression;
    }
    public dom_Block getDom_block() {
        return dom_block;
    }

    public void setDom_block(dom_Block dom_block) {
        this.dom_block = dom_block;
    }
    public dom_Expression getDom_expression() {
        return dom_expression;
    }

    public void setDom_expression(dom_Expression dom_expression) {
        this.dom_expression = dom_expression;
    }

}