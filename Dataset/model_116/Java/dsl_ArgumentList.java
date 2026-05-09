





import java.util.List;
import java.util.ArrayList;

public class dsl_ArgumentList  {






    private dsl_Arguments dsl_arguments;




    private List<dsl_Expression> dsl_expressions;


    public dsl_ArgumentList(
    ) {
        this.dsl_expressions = new ArrayList<>();
    }

    public dsl_ArgumentList(
        ArrayList<dsl_Expression> dsl_expressions    ) {
        this.dsl_expressions = dsl_expressions;
    }


    public dsl_Arguments getDsl_arguments() {
        return dsl_arguments;
    }

    public void setDsl_arguments(dsl_Arguments dsl_arguments) {
        this.dsl_arguments = dsl_arguments;
    }
    public List<dsl_Expression> getDsl_expressions() {
        return dsl_expressions;
    }

    public void addDsl_expression(Dsl_expression dsl_expression) {
        this.dsl_expressions.add(dsl_expression);
    }

}