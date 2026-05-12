





import java.util.List;
import java.util.ArrayList;

public class sql_value_FunctionValue extends Value {

    private String functionName;





    private List<value_Value> value_values;


    public sql_value_FunctionValue(
        String functionName    ) {
        super(
        );
        this.functionName = functionName;
        this.value_values = new ArrayList<>();
    }

    public sql_value_FunctionValue(
        String functionName        ArrayList<value_Value> value_values    ) {
        this.functionName = functionName;
        this.value_values = value_values;
    }

    public String getFunctionname() {
        return functionName;
    }

    public void setFunctionname(String functionName) {
        this.functionName = functionName;
    }

    public List<value_Value> getValue_values() {
        return value_values;
    }

    public void addValue_value(Value_value value_value) {
        this.value_values.add(value_value);
    }

}