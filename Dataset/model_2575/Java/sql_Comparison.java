





import java.util.List;
import java.util.ArrayList;

public class sql_Comparison  {

    private String subOperator;
    private String operator;



    public sql_Comparison(
        String subOperator,        String operator    ) {
        this.subOperator = subOperator;
        this.operator = operator;
    }


    public String getSuboperator() {
        return subOperator;
    }

    public void setSuboperator(String subOperator) {
        this.subOperator = subOperator;
    }
    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }


}