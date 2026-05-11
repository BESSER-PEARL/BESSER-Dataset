





import java.util.List;
import java.util.ArrayList;

public class gaml_Expression  {

    private String op;





    private gaml_Expression gaml_expression;




    private gaml_StringEvaluator gaml_stringevaluator;




    private gaml_Expression gaml_expression;




    private gaml_Block gaml_block;




    private gaml_Facet gaml_facet;


    public gaml_Expression(
        String op    ) {
        this.op = op;
    }


    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }

    public gaml_Expression getGaml_expression() {
        return gaml_expression;
    }

    public void setGaml_expression(gaml_Expression gaml_expression) {
        this.gaml_expression = gaml_expression;
    }
    public gaml_StringEvaluator getGaml_stringevaluator() {
        return gaml_stringevaluator;
    }

    public void setGaml_stringevaluator(gaml_StringEvaluator gaml_stringevaluator) {
        this.gaml_stringevaluator = gaml_stringevaluator;
    }
    public gaml_Expression getGaml_expression() {
        return gaml_expression;
    }

    public void setGaml_expression(gaml_Expression gaml_expression) {
        this.gaml_expression = gaml_expression;
    }
    public gaml_Block getGaml_block() {
        return gaml_block;
    }

    public void setGaml_block(gaml_Block gaml_block) {
        this.gaml_block = gaml_block;
    }
    public gaml_Facet getGaml_facet() {
        return gaml_facet;
    }

    public void setGaml_facet(gaml_Facet gaml_facet) {
        this.gaml_facet = gaml_facet;
    }

}