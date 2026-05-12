





import java.util.List;
import java.util.ArrayList;

public class expression_ExpressionOperationNot  {






    private sql_condition_IsNullCondition sql_condition_isnullcondition;




    private sql_condition_LikeCondition sql_condition_likecondition;




    private sql_expression_SimpleExpression sql_expression_simpleexpression;




    private sql_condition_InCondition sql_condition_incondition;


    public expression_ExpressionOperationNot(
    ) {
    }



    public sql_condition_IsNullCondition getSql_condition_isnullcondition() {
        return sql_condition_isnullcondition;
    }

    public void setSql_condition_isnullcondition(sql_condition_IsNullCondition sql_condition_isnullcondition) {
        this.sql_condition_isnullcondition = sql_condition_isnullcondition;
    }
    public sql_condition_LikeCondition getSql_condition_likecondition() {
        return sql_condition_likecondition;
    }

    public void setSql_condition_likecondition(sql_condition_LikeCondition sql_condition_likecondition) {
        this.sql_condition_likecondition = sql_condition_likecondition;
    }
    public sql_expression_SimpleExpression getSql_expression_simpleexpression() {
        return sql_expression_simpleexpression;
    }

    public void setSql_expression_simpleexpression(sql_expression_SimpleExpression sql_expression_simpleexpression) {
        this.sql_expression_simpleexpression = sql_expression_simpleexpression;
    }
    public sql_condition_InCondition getSql_condition_incondition() {
        return sql_condition_incondition;
    }

    public void setSql_condition_incondition(sql_condition_InCondition sql_condition_incondition) {
        this.sql_condition_incondition = sql_condition_incondition;
    }

}