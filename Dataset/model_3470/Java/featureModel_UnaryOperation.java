





import java.util.List;
import java.util.ArrayList;

public class featureModel_UnaryOperation extends Expression {

    private String operator;



    public featureModel_UnaryOperation(
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