





import java.util.List;
import java.util.ArrayList;

public class diagram_TypedVariableValue extends VariableValue {

    private String value;





    private TypedVariable typedvariable;


    public diagram_TypedVariableValue(
        String value    ) {
        super(
        );
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public TypedVariable getTypedvariable() {
        return typedvariable;
    }

    public void setTypedvariable(TypedVariable typedvariable) {
        this.typedvariable = typedvariable;
    }

}