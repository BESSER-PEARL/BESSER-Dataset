





import java.util.List;
import java.util.ArrayList;

public class odemcustom_ArgumentExpression  {






    private List<odemcustom_Expression> odemcustom_expressions;




    private odemcustom_IdExpr odemcustom_idexpr;


    public odemcustom_ArgumentExpression(
    ) {
        this.odemcustom_expressions = new ArrayList<>();
    }

    public odemcustom_ArgumentExpression(
        ArrayList<odemcustom_Expression> odemcustom_expressions    ) {
        this.odemcustom_expressions = odemcustom_expressions;
    }


    public List<odemcustom_Expression> getOdemcustom_expressions() {
        return odemcustom_expressions;
    }

    public void addOdemcustom_expression(Odemcustom_expression odemcustom_expression) {
        this.odemcustom_expressions.add(odemcustom_expression);
    }
    public odemcustom_IdExpr getOdemcustom_idexpr() {
        return odemcustom_idexpr;
    }

    public void setOdemcustom_idexpr(odemcustom_IdExpr odemcustom_idexpr) {
        this.odemcustom_idexpr = odemcustom_idexpr;
    }

}