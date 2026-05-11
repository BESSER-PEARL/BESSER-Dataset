





import java.util.List;
import java.util.ArrayList;

public class simple_lang_FeatureCallExpression extends Expression {

    private String name;





    private simple_lang_Expression simple_lang_expression;


    public simple_lang_FeatureCallExpression(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public simple_lang_Expression getSimple_lang_expression() {
        return simple_lang_expression;
    }

    public void setSimple_lang_expression(simple_lang_Expression simple_lang_expression) {
        this.simple_lang_expression = simple_lang_expression;
    }

}