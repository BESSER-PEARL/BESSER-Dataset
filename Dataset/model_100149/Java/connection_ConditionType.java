





import java.util.List;
import java.util.ArrayList;

public class connection_ConditionType  {

    private String function;
    private String value;
    private String operator;
    private String inputColumn;





    private connection_ValidationRulesConnection connection_validationrulesconnection;


    public connection_ConditionType(
        String function,        String value,        String operator,        String inputColumn    ) {
        this.function = function;
        this.value = value;
        this.operator = operator;
        this.inputColumn = inputColumn;
    }


    public String getFunction() {
        return function;
    }

    public void setFunction(String function) {
        this.function = function;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }
    public String getInputcolumn() {
        return inputColumn;
    }

    public void setInputcolumn(String inputColumn) {
        this.inputColumn = inputColumn;
    }

    public connection_ValidationRulesConnection getConnection_validationrulesconnection() {
        return connection_validationrulesconnection;
    }

    public void setConnection_validationrulesconnection(connection_ValidationRulesConnection connection_validationrulesconnection) {
        this.connection_validationrulesconnection = connection_validationrulesconnection;
    }

}