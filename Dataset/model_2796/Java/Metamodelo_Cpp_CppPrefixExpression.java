





import java.util.List;
import java.util.ArrayList;

public class Metamodelo_Cpp_CppPrefixExpression extends CppUnaryExpression {

    private String operator;



    public Metamodelo_Cpp_CppPrefixExpression(
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