





import java.util.List;
import java.util.ArrayList;

public class pascal_simpleExpression  {

    private String additiveoperator;





    private pascal_simpleExpression pascal_simpleexpression;




    private pascal_expression pascal_expression;


    public pascal_simpleExpression(
        String additiveoperator    ) {
        this.additiveoperator = additiveoperator;
    }


    public String getAdditiveoperator() {
        return additiveoperator;
    }

    public void setAdditiveoperator(String additiveoperator) {
        this.additiveoperator = additiveoperator;
    }

    public pascal_simpleExpression getPascal_simpleexpression() {
        return pascal_simpleexpression;
    }

    public void setPascal_simpleexpression(pascal_simpleExpression pascal_simpleexpression) {
        this.pascal_simpleexpression = pascal_simpleexpression;
    }
    public pascal_expression getPascal_expression() {
        return pascal_expression;
    }

    public void setPascal_expression(pascal_expression pascal_expression) {
        this.pascal_expression = pascal_expression;
    }

}