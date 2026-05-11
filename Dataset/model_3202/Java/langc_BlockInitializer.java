





import java.util.List;
import java.util.ArrayList;

public class langc_BlockInitializer extends Expression {






    private List<langc_Expression> langc_expressions;


    public langc_BlockInitializer(
    ) {
        super(
        );
        this.langc_expressions = new ArrayList<>();
    }

    public langc_BlockInitializer(
        ArrayList<langc_Expression> langc_expressions    ) {
        this.langc_expressions = langc_expressions;
    }


    public List<langc_Expression> getLangc_expressions() {
        return langc_expressions;
    }

    public void addLangc_expression(Langc_expression langc_expression) {
        this.langc_expressions.add(langc_expression);
    }

}