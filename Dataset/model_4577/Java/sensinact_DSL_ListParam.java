





import java.util.List;
import java.util.ArrayList;

public class sensinact_DSL_ListParam  {






    private List<sensinact_DSL_Expression> sensinact_dsl_expressions;




    private sensinact_DSL_ResourceAction sensinact_dsl_resourceaction;


    public sensinact_DSL_ListParam(
    ) {
        this.sensinact_dsl_expressions = new ArrayList<>();
    }

    public sensinact_DSL_ListParam(
        ArrayList<sensinact_DSL_Expression> sensinact_dsl_expressions    ) {
        this.sensinact_dsl_expressions = sensinact_dsl_expressions;
    }


    public List<sensinact_DSL_Expression> getSensinact_dsl_expressions() {
        return sensinact_dsl_expressions;
    }

    public void addSensinact_dsl_expression(Sensinact_dsl_expression sensinact_dsl_expression) {
        this.sensinact_dsl_expressions.add(sensinact_dsl_expression);
    }
    public sensinact_DSL_ResourceAction getSensinact_dsl_resourceaction() {
        return sensinact_dsl_resourceaction;
    }

    public void setSensinact_dsl_resourceaction(sensinact_DSL_ResourceAction sensinact_dsl_resourceaction) {
        this.sensinact_dsl_resourceaction = sensinact_dsl_resourceaction;
    }

}