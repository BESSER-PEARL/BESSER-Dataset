





import java.util.List;
import java.util.ArrayList;

public class connection_ConditionType  {

    private String operator;
    private String function;
    private String inputColumn;
    private String value;



    public connection_ConditionType(
        String operator,        String function,        String inputColumn,        String value    ) {
        this.operator = operator;
        this.function = function;
        this.inputColumn = inputColumn;
        this.value = value;
    }


    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }
    public String getFunction() {
        return function;
    }

    public void setFunction(String function) {
        this.function = function;
    }
    public String getInputcolumn() {
        return inputColumn;
    }

    public void setInputcolumn(String inputColumn) {
        this.inputColumn = inputColumn;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}