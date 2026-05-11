





import java.util.List;
import java.util.ArrayList;

public class parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression extends Expression {

    private String _property;





    private parameterizedExpressionsTestLanguage_Expression parameterizedexpressionstestlanguage_expression;


    public parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression(
        String _property    ) {
        super(
        );
        this._property = _property;
    }


    public String get_property() {
        return _property;
    }

    public void set_property(String _property) {
        this._property = _property;
    }

    public parameterizedExpressionsTestLanguage_Expression getParameterizedexpressionstestlanguage_expression() {
        return parameterizedexpressionstestlanguage_expression;
    }

    public void setParameterizedexpressionstestlanguage_expression(parameterizedExpressionsTestLanguage_Expression parameterizedexpressionstestlanguage_expression) {
        this.parameterizedexpressionstestlanguage_expression = parameterizedexpressionstestlanguage_expression;
    }

}