





import java.util.List;
import java.util.ArrayList;

public class DOM_VariableDeclaration extends ASTNode {

    private String extraDimensions;





    private DOM_Expression dom_expression;


    public DOM_VariableDeclaration(
        String extraDimensions    ) {
        super(
        );
        this.extraDimensions = extraDimensions;
    }


    public String getExtradimensions() {
        return extraDimensions;
    }

    public void setExtradimensions(String extraDimensions) {
        this.extraDimensions = extraDimensions;
    }

    public DOM_Expression getDom_expression() {
        return dom_expression;
    }

    public void setDom_expression(DOM_Expression dom_expression) {
        this.dom_expression = dom_expression;
    }

}