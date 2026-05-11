





import java.util.List;
import java.util.ArrayList;

public class SMTlib2extended_NAryExpression extends Expression {






    private List<SMTlib2extended_Expression> smtlib2extended_expressions;


    public SMTlib2extended_NAryExpression(
    ) {
        super(
        );
        this.smtlib2extended_expressions = new ArrayList<>();
    }

    public SMTlib2extended_NAryExpression(
        ArrayList<SMTlib2extended_Expression> smtlib2extended_expressions    ) {
        this.smtlib2extended_expressions = smtlib2extended_expressions;
    }


    public List<SMTlib2extended_Expression> getSmtlib2extended_expressions() {
        return smtlib2extended_expressions;
    }

    public void addSmtlib2extended_expression(Smtlib2extended_expression smtlib2extended_expression) {
        this.smtlib2extended_expressions.add(smtlib2extended_expression);
    }

}