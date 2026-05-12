





import java.util.List;
import java.util.ArrayList;

public class sql_Comparison  {

    private String subOperator;
    private String operator;





    private sql_FullExpression sql_fullexpression;




    private sql_Operands sql_operands;


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

    public sql_FullExpression getSql_fullexpression() {
        return sql_fullexpression;
    }

    public void setSql_fullexpression(sql_FullExpression sql_fullexpression) {
        this.sql_fullexpression = sql_fullexpression;
    }
    public sql_Operands getSql_operands() {
        return sql_operands;
    }

    public void setSql_operands(sql_Operands sql_operands) {
        this.sql_operands = sql_operands;
    }

}