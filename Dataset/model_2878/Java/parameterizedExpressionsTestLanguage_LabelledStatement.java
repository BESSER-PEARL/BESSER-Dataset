





import java.util.List;
import java.util.ArrayList;

public class parameterizedExpressionsTestLanguage_LabelledStatement extends Statement {

    private String name;





    private parameterizedExpressionsTestLanguage_Statement parameterizedexpressionstestlanguage_statement;


    public parameterizedExpressionsTestLanguage_LabelledStatement(
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

    public parameterizedExpressionsTestLanguage_Statement getParameterizedexpressionstestlanguage_statement() {
        return parameterizedexpressionstestlanguage_statement;
    }

    public void setParameterizedexpressionstestlanguage_statement(parameterizedExpressionsTestLanguage_Statement parameterizedexpressionstestlanguage_statement) {
        this.parameterizedexpressionstestlanguage_statement = parameterizedexpressionstestlanguage_statement;
    }

}