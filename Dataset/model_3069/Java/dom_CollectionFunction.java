





import java.util.List;
import java.util.ArrayList;

public class dom_CollectionFunction extends Expression {

    private String function;





    private dom_PropertyValue dom_propertyvalue;


    public dom_CollectionFunction(
        String function    ) {
        super(
        );
        this.function = function;
    }


    public String getFunction() {
        return function;
    }

    public void setFunction(String function) {
        this.function = function;
    }

    public dom_PropertyValue getDom_propertyvalue() {
        return dom_propertyvalue;
    }

    public void setDom_propertyvalue(dom_PropertyValue dom_propertyvalue) {
        this.dom_propertyvalue = dom_propertyvalue;
    }

}