





import java.util.List;
import java.util.ArrayList;

public class eol_CollectionExpression extends Expression {






    private List<eol_Expression> eol_expressions;


    public eol_CollectionExpression(
    ) {
        super(
        );
        this.eol_expressions = new ArrayList<>();
    }

    public eol_CollectionExpression(
        ArrayList<eol_Expression> eol_expressions    ) {
        this.eol_expressions = eol_expressions;
    }


    public List<eol_Expression> getEol_expressions() {
        return eol_expressions;
    }

    public void addEol_expression(Eol_expression eol_expression) {
        this.eol_expressions.add(eol_expression);
    }

}