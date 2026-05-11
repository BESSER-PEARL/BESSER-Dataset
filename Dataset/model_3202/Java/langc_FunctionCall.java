





import java.util.List;
import java.util.ArrayList;

public class langc_FunctionCall extends Expression {






    private List<langc_Expression> langc_expressions;




    private langc_Function langc_function;


    public langc_FunctionCall(
    ) {
        super(
        );
        this.langc_expressions = new ArrayList<>();
    }

    public langc_FunctionCall(
        ArrayList<langc_Expression> langc_expressions    ) {
        this.langc_expressions = langc_expressions;
    }


    public List<langc_Expression> getLangc_expressions() {
        return langc_expressions;
    }

    public void addLangc_expression(Langc_expression langc_expression) {
        this.langc_expressions.add(langc_expression);
    }
    public langc_Function getLangc_function() {
        return langc_function;
    }

    public void setLangc_function(langc_Function langc_function) {
        this.langc_function = langc_function;
    }

}