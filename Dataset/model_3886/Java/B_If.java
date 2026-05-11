





import java.util.List;
import java.util.ArrayList;

public class B_If extends Expression {






    private List<B_Predicate> b_predicates;




    private List<B_Expression> b_expressions;




    private List<B_Expression> b_expressions;


    public B_If(
    ) {
        super(
        );
        this.b_predicates = new ArrayList<>();
        this.b_expressions = new ArrayList<>();
        this.b_expressions = new ArrayList<>();
    }

    public B_If(
        ArrayList<B_Predicate> b_predicates,        ArrayList<B_Expression> b_expressions,        ArrayList<B_Expression> b_expressions    ) {
        this.b_predicates = b_predicates;
        this.b_expressions = b_expressions;
        this.b_expressions = b_expressions;
    }


    public List<B_Predicate> getB_predicates() {
        return b_predicates;
    }

    public void addB_predicate(B_predicate b_predicate) {
        this.b_predicates.add(b_predicate);
    }
    public List<B_Expression> getB_expressions() {
        return b_expressions;
    }

    public void addB_expression(B_expression b_expression) {
        this.b_expressions.add(b_expression);
    }
    public List<B_Expression> getB_expressions() {
        return b_expressions;
    }

    public void addB_expression(B_expression b_expression) {
        this.b_expressions.add(b_expression);
    }

}