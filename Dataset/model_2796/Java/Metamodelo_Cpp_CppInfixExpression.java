





import java.util.List;
import java.util.ArrayList;

public class Metamodelo_Cpp_CppInfixExpression extends CppBinaryExpression {

    private String operator;



    public Metamodelo_Cpp_CppInfixExpression(
        String operator    ) {
        super(
        );
        this.operator = operator;
    }


    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }


}