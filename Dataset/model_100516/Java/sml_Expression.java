





import java.util.List;
import java.util.ArrayList;

public class sml_Expression extends ExpressionAndVariables {






    private sml_ExpressionParameter sml_expressionparameter;




    private sml_UnaryOperationExpression sml_unaryoperationexpression;




    private sml_BinaryOperationExpression sml_binaryoperationexpression;




    private sml_BinaryOperationExpression sml_binaryoperationexpression;




    private sml_CollectionAccess sml_collectionaccess;




    private sml_VariableExpression sml_variableexpression;


    public sml_Expression(
    ) {
        super(
        );
    }



    public sml_ExpressionParameter getSml_expressionparameter() {
        return sml_expressionparameter;
    }

    public void setSml_expressionparameter(sml_ExpressionParameter sml_expressionparameter) {
        this.sml_expressionparameter = sml_expressionparameter;
    }
    public sml_UnaryOperationExpression getSml_unaryoperationexpression() {
        return sml_unaryoperationexpression;
    }

    public void setSml_unaryoperationexpression(sml_UnaryOperationExpression sml_unaryoperationexpression) {
        this.sml_unaryoperationexpression = sml_unaryoperationexpression;
    }
    public sml_BinaryOperationExpression getSml_binaryoperationexpression() {
        return sml_binaryoperationexpression;
    }

    public void setSml_binaryoperationexpression(sml_BinaryOperationExpression sml_binaryoperationexpression) {
        this.sml_binaryoperationexpression = sml_binaryoperationexpression;
    }
    public sml_BinaryOperationExpression getSml_binaryoperationexpression() {
        return sml_binaryoperationexpression;
    }

    public void setSml_binaryoperationexpression(sml_BinaryOperationExpression sml_binaryoperationexpression) {
        this.sml_binaryoperationexpression = sml_binaryoperationexpression;
    }
    public sml_CollectionAccess getSml_collectionaccess() {
        return sml_collectionaccess;
    }

    public void setSml_collectionaccess(sml_CollectionAccess sml_collectionaccess) {
        this.sml_collectionaccess = sml_collectionaccess;
    }
    public sml_VariableExpression getSml_variableexpression() {
        return sml_variableexpression;
    }

    public void setSml_variableexpression(sml_VariableExpression sml_variableexpression) {
        this.sml_variableexpression = sml_variableexpression;
    }

}