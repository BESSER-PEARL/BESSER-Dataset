





import java.util.List;
import java.util.ArrayList;

public class minilang_VariableAffect extends Statement {






    private minilang_Value minilang_value;




    private minilang_Variable minilang_variable;


    public minilang_VariableAffect(
    ) {
        super(
        );
    }



    public minilang_Value getMinilang_value() {
        return minilang_value;
    }

    public void setMinilang_value(minilang_Value minilang_value) {
        this.minilang_value = minilang_value;
    }
    public minilang_Variable getMinilang_variable() {
        return minilang_variable;
    }

    public void setMinilang_variable(minilang_Variable minilang_variable) {
        this.minilang_variable = minilang_variable;
    }

}