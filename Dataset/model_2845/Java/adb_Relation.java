





import java.util.List;
import java.util.ArrayList;

public class adb_Relation  {

    private String relationalOperator;





    private adb_SimpleExpression adb_simpleexpression;




    private adb_SimpleExpression adb_simpleexpression;




    private adb_Expression adb_expression;


    public adb_Relation(
        String relationalOperator    ) {
        this.relationalOperator = relationalOperator;
    }


    public String getRelationaloperator() {
        return relationalOperator;
    }

    public void setRelationaloperator(String relationalOperator) {
        this.relationalOperator = relationalOperator;
    }

    public adb_SimpleExpression getAdb_simpleexpression() {
        return adb_simpleexpression;
    }

    public void setAdb_simpleexpression(adb_SimpleExpression adb_simpleexpression) {
        this.adb_simpleexpression = adb_simpleexpression;
    }
    public adb_SimpleExpression getAdb_simpleexpression() {
        return adb_simpleexpression;
    }

    public void setAdb_simpleexpression(adb_SimpleExpression adb_simpleexpression) {
        this.adb_simpleexpression = adb_simpleexpression;
    }
    public adb_Expression getAdb_expression() {
        return adb_expression;
    }

    public void setAdb_expression(adb_Expression adb_expression) {
        this.adb_expression = adb_expression;
    }

}