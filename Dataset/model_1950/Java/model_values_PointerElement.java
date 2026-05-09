





import java.util.List;
import java.util.ArrayList;

public class model_values_PointerElement  {

    private String index;





    private Variable variable;




    private Type type;


    public model_values_PointerElement(
        String index    ) {
        this.index = index;
    }


    public String getIndex() {
        return index;
    }

    public void setIndex(String index) {
        this.index = index;
    }

    public Variable getVariable() {
        return variable;
    }

    public void setVariable(Variable variable) {
        this.variable = variable;
    }
    public Type getType() {
        return type;
    }

    public void setType(Type type) {
        this.type = type;
    }

}