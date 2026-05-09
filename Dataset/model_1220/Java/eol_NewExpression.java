





import java.util.List;
import java.util.ArrayList;

public class eol_NewExpression extends Expression {






    private List<eol_Expression> eol_expressions;




    private eol_NameExpression eol_nameexpression;


    public eol_NewExpression(
    ) {
        super(
        );
        this.eol_expressions = new ArrayList<>();
    }

    public eol_NewExpression(
        ArrayList<eol_Expression> eol_expressions    ) {
        this.eol_expressions = eol_expressions;
    }


    public List<eol_Expression> getEol_expressions() {
        return eol_expressions;
    }

    public void addEol_expression(Eol_expression eol_expression) {
        this.eol_expressions.add(eol_expression);
    }
    public eol_NameExpression getEol_nameexpression() {
        return eol_nameexpression;
    }

    public void setEol_nameexpression(eol_NameExpression eol_nameexpression) {
        this.eol_nameexpression = eol_nameexpression;
    }

}