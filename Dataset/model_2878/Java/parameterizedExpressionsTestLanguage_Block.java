





import java.util.List;
import java.util.ArrayList;

public class parameterizedExpressionsTestLanguage_Block extends Statement {






    private List<parameterizedExpressionsTestLanguage_Statement> parameterizedexpressionstestlanguage_statements;




    private parameterizedExpressionsTestLanguage_FunctionDeclaration parameterizedexpressionstestlanguage_functiondeclaration;


    public parameterizedExpressionsTestLanguage_Block(
    ) {
        super(
        );
        this.parameterizedexpressionstestlanguage_statements = new ArrayList<>();
    }

    public parameterizedExpressionsTestLanguage_Block(
        ArrayList<parameterizedExpressionsTestLanguage_Statement> parameterizedexpressionstestlanguage_statements    ) {
        this.parameterizedexpressionstestlanguage_statements = parameterizedexpressionstestlanguage_statements;
    }


    public List<parameterizedExpressionsTestLanguage_Statement> getParameterizedexpressionstestlanguage_statements() {
        return parameterizedexpressionstestlanguage_statements;
    }

    public void addParameterizedexpressionstestlanguage_statement(Parameterizedexpressionstestlanguage_statement parameterizedexpressionstestlanguage_statement) {
        this.parameterizedexpressionstestlanguage_statements.add(parameterizedexpressionstestlanguage_statement);
    }
    public parameterizedExpressionsTestLanguage_FunctionDeclaration getParameterizedexpressionstestlanguage_functiondeclaration() {
        return parameterizedexpressionstestlanguage_functiondeclaration;
    }

    public void setParameterizedexpressionstestlanguage_functiondeclaration(parameterizedExpressionsTestLanguage_FunctionDeclaration parameterizedexpressionstestlanguage_functiondeclaration) {
        this.parameterizedexpressionstestlanguage_functiondeclaration = parameterizedexpressionstestlanguage_functiondeclaration;
    }

}