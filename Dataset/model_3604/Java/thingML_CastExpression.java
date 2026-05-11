





import java.util.List;
import java.util.ArrayList;

public class thingML_CastExpression extends Expression {

    private boolean isArray;





    private thingML_Expression thingml_expression;




    private thingML_Type thingml_type;


    public thingML_CastExpression(
        boolean isArray    ) {
        super(
        );
        this.isArray = isArray;
    }


    public boolean getIsarray() {
        return isArray;
    }

    public void setIsarray(boolean isArray) {
        this.isArray = isArray;
    }

    public thingML_Expression getThingml_expression() {
        return thingml_expression;
    }

    public void setThingml_expression(thingML_Expression thingml_expression) {
        this.thingml_expression = thingml_expression;
    }
    public thingML_Type getThingml_type() {
        return thingml_type;
    }

    public void setThingml_type(thingML_Type thingml_type) {
        this.thingml_type = thingml_type;
    }

}