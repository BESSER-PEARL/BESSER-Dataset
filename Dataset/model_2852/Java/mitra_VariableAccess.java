





import java.util.List;
import java.util.ArrayList;

public class mitra_VariableAccess extends TerminalExpression, StatementExpression {

    private String postfixOperator;
    private String prefixOperator;





    private mitra_Expression mitra_expression;




    private mitra_VarDeclaration mitra_vardeclaration;


    public mitra_VariableAccess(
        String postfixOperator,        String prefixOperator    ) {
        super(
        );
        this.postfixOperator = postfixOperator;
        this.prefixOperator = prefixOperator;
    }


    public String getPostfixoperator() {
        return postfixOperator;
    }

    public void setPostfixoperator(String postfixOperator) {
        this.postfixOperator = postfixOperator;
    }
    public String getPrefixoperator() {
        return prefixOperator;
    }

    public void setPrefixoperator(String prefixOperator) {
        this.prefixOperator = prefixOperator;
    }

    public mitra_Expression getMitra_expression() {
        return mitra_expression;
    }

    public void setMitra_expression(mitra_Expression mitra_expression) {
        this.mitra_expression = mitra_expression;
    }
    public mitra_VarDeclaration getMitra_vardeclaration() {
        return mitra_vardeclaration;
    }

    public void setMitra_vardeclaration(mitra_VarDeclaration mitra_vardeclaration) {
        this.mitra_vardeclaration = mitra_vardeclaration;
    }

}