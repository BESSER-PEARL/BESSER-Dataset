





import java.util.List;
import java.util.ArrayList;

public class eol_ExprList extends CollectionInitValue {






    private List<eol_Expression> eol_expressions;


    public eol_ExprList(
    ) {
        super(
        );
        this.eol_expressions = new ArrayList<>();
    }

    public eol_ExprList(
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