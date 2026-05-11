





import java.util.List;
import java.util.ArrayList;

public class haxe_HaxePrefixExpression extends HaxeUnaryExpression {

    private String operator;



    public haxe_HaxePrefixExpression(
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