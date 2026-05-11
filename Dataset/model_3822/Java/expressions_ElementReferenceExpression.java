





import java.util.List;
import java.util.ArrayList;

public class expressions_ElementReferenceExpression extends ArgumentExpression {

    private boolean operationCall;
    private boolean arrayAccess;





    private List<expressions_Expression> expressions_expressions;




    private expressions_EObject expressions_eobject;


    public expressions_ElementReferenceExpression(
        boolean operationCall,        boolean arrayAccess    ) {
        super(
        );
        this.operationCall = operationCall;
        this.arrayAccess = arrayAccess;
        this.expressions_expressions = new ArrayList<>();
    }

    public expressions_ElementReferenceExpression(
        boolean operationCall,        boolean arrayAccess        ArrayList<expressions_Expression> expressions_expressions    ) {
        this.operationCall = operationCall;
        this.arrayAccess = arrayAccess;
        this.expressions_expressions = expressions_expressions;
    }

    public boolean getOperationcall() {
        return operationCall;
    }

    public void setOperationcall(boolean operationCall) {
        this.operationCall = operationCall;
    }
    public boolean getArrayaccess() {
        return arrayAccess;
    }

    public void setArrayaccess(boolean arrayAccess) {
        this.arrayAccess = arrayAccess;
    }

    public List<expressions_Expression> getExpressions_expressions() {
        return expressions_expressions;
    }

    public void addExpressions_expression(Expressions_expression expressions_expression) {
        this.expressions_expressions.add(expressions_expression);
    }
    public expressions_EObject getExpressions_eobject() {
        return expressions_eobject;
    }

    public void setExpressions_eobject(expressions_EObject expressions_eobject) {
        this.expressions_eobject = expressions_eobject;
    }

}