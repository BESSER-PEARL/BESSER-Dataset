





import java.util.List;
import java.util.ArrayList;

public class thingML_TypeRef  {

    private boolean isArray;





    private thingML_Parameter thingml_parameter;




    private thingML_LocalVariable thingml_localvariable;




    private thingML_Property thingml_property;




    private thingML_Expression thingml_expression;




    private thingML_Type thingml_type;




    private thingML_Function thingml_function;


    public thingML_TypeRef(
        boolean isArray    ) {
        this.isArray = isArray;
    }


    public boolean getIsarray() {
        return isArray;
    }

    public void setIsarray(boolean isArray) {
        this.isArray = isArray;
    }

    public thingML_Parameter getThingml_parameter() {
        return thingml_parameter;
    }

    public void setThingml_parameter(thingML_Parameter thingml_parameter) {
        this.thingml_parameter = thingml_parameter;
    }
    public thingML_LocalVariable getThingml_localvariable() {
        return thingml_localvariable;
    }

    public void setThingml_localvariable(thingML_LocalVariable thingml_localvariable) {
        this.thingml_localvariable = thingml_localvariable;
    }
    public thingML_Property getThingml_property() {
        return thingml_property;
    }

    public void setThingml_property(thingML_Property thingml_property) {
        this.thingml_property = thingml_property;
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
    public thingML_Function getThingml_function() {
        return thingml_function;
    }

    public void setThingml_function(thingML_Function thingml_function) {
        this.thingml_function = thingml_function;
    }

}