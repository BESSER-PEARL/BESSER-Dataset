





import java.util.List;
import java.util.ArrayList;

public class simple_lang_MethodCallExpression extends FeatureCallExpression {






    private List<simple_lang_Expression> simple_lang_expressions;


    public simple_lang_MethodCallExpression(
    ) {
        super(
        );
        this.simple_lang_expressions = new ArrayList<>();
    }

    public simple_lang_MethodCallExpression(
        ArrayList<simple_lang_Expression> simple_lang_expressions    ) {
        this.simple_lang_expressions = simple_lang_expressions;
    }


    public List<simple_lang_Expression> getSimple_lang_expressions() {
        return simple_lang_expressions;
    }

    public void addSimple_lang_expression(Simple_lang_expression simple_lang_expression) {
        this.simple_lang_expressions.add(simple_lang_expression);
    }

}