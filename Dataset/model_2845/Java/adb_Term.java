





import java.util.List;
import java.util.ArrayList;

public class adb_Term  {

    private String multiplyingOperators;





    private adb_SimpleExpression adb_simpleexpression;


    public adb_Term(
        String multiplyingOperators    ) {
        this.multiplyingOperators = multiplyingOperators;
    }


    public String getMultiplyingoperators() {
        return multiplyingOperators;
    }

    public void setMultiplyingoperators(String multiplyingOperators) {
        this.multiplyingOperators = multiplyingOperators;
    }

    public adb_SimpleExpression getAdb_simpleexpression() {
        return adb_simpleexpression;
    }

    public void setAdb_simpleexpression(adb_SimpleExpression adb_simpleexpression) {
        this.adb_simpleexpression = adb_simpleexpression;
    }

}