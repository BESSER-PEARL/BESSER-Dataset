





import java.util.List;
import java.util.ArrayList;

public class haxe_HaxeInfixExpression extends HaxeBinaryExpression {

    private String operator;





    private List<haxe_HaxeExpression> haxe_haxeexpressions;


    public haxe_HaxeInfixExpression(
        String operator    ) {
        super(
        );
        this.operator = operator;
        this.haxe_haxeexpressions = new ArrayList<>();
    }

    public haxe_HaxeInfixExpression(
        String operator        ArrayList<haxe_HaxeExpression> haxe_haxeexpressions    ) {
        this.operator = operator;
        this.haxe_haxeexpressions = haxe_haxeexpressions;
    }

    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public List<haxe_HaxeExpression> getHaxe_haxeexpressions() {
        return haxe_haxeexpressions;
    }

    public void addHaxe_haxeexpression(Haxe_haxeexpression haxe_haxeexpression) {
        this.haxe_haxeexpressions.add(haxe_haxeexpression);
    }

}