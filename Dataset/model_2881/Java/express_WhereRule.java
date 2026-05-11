





import java.util.List;
import java.util.ArrayList;

public class express_WhereRule  {

    private String name;
    private String expression;





    private express_ExpressConcept express_expressconcept;




    private express_Rule express_rule;


    public express_WhereRule(
        String name,        String expression    ) {
        this.name = name;
        this.expression = expression;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getExpression() {
        return expression;
    }

    public void setExpression(String expression) {
        this.expression = expression;
    }

    public express_ExpressConcept getExpress_expressconcept() {
        return express_expressconcept;
    }

    public void setExpress_expressconcept(express_ExpressConcept express_expressconcept) {
        this.express_expressconcept = express_expressconcept;
    }
    public express_Rule getExpress_rule() {
        return express_rule;
    }

    public void setExpress_rule(express_Rule express_rule) {
        this.express_rule = express_rule;
    }

}