





import java.util.List;
import java.util.ArrayList;

public class codemodel_expressions_BinExp extends Expression {

    private String operator;



    public codemodel_expressions_BinExp(
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