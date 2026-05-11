





import java.util.List;
import java.util.ArrayList;

public class eol_expression_CollectionExpression extends Expression {






    private List<eol_expression_Expression> eol_expression_expressions;




    private eol_expression_CollectionInitialisationExpression eol_expression_collectioninitialisationexpression;


    public eol_expression_CollectionExpression(
    ) {
        super(
        );
        this.eol_expression_expressions = new ArrayList<>();
    }

    public eol_expression_CollectionExpression(
        ArrayList<eol_expression_Expression> eol_expression_expressions    ) {
        this.eol_expression_expressions = eol_expression_expressions;
    }


    public List<eol_expression_Expression> getEol_expression_expressions() {
        return eol_expression_expressions;
    }

    public void addEol_expression_expression(Eol_expression_expression eol_expression_expression) {
        this.eol_expression_expressions.add(eol_expression_expression);
    }
    public eol_expression_CollectionInitialisationExpression getEol_expression_collectioninitialisationexpression() {
        return eol_expression_collectioninitialisationexpression;
    }

    public void setEol_expression_collectioninitialisationexpression(eol_expression_CollectionInitialisationExpression eol_expression_collectioninitialisationexpression) {
        this.eol_expression_collectioninitialisationexpression = eol_expression_collectioninitialisationexpression;
    }

}