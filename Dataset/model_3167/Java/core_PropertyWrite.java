





import java.util.List;
import java.util.ArrayList;

public class core_PropertyWrite extends Expression {

    private String _property;





    private core_Expression core_expression;




    private core_Variable core_variable;


    public core_PropertyWrite(
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

    public core_Expression getCore_expression() {
        return core_expression;
    }

    public void setCore_expression(core_Expression core_expression) {
        this.core_expression = core_expression;
    }
    public core_Variable getCore_variable() {
        return core_variable;
    }

    public void setCore_variable(core_Variable core_variable) {
        this.core_variable = core_variable;
    }

}