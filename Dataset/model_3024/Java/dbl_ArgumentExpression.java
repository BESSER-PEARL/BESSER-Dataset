





import java.util.List;
import java.util.ArrayList;

public class dbl_ArgumentExpression  {






    private dbl_IdExpr dbl_idexpr;




    private List<dbl_Expression> dbl_expressions;




    private dbl_AddToSet dbl_addtoset;


    public dbl_ArgumentExpression(
    ) {
        this.dbl_expressions = new ArrayList<>();
    }

    public dbl_ArgumentExpression(
        ArrayList<dbl_Expression> dbl_expressions    ) {
        this.dbl_expressions = dbl_expressions;
    }


    public dbl_IdExpr getDbl_idexpr() {
        return dbl_idexpr;
    }

    public void setDbl_idexpr(dbl_IdExpr dbl_idexpr) {
        this.dbl_idexpr = dbl_idexpr;
    }
    public List<dbl_Expression> getDbl_expressions() {
        return dbl_expressions;
    }

    public void addDbl_expression(Dbl_expression dbl_expression) {
        this.dbl_expressions.add(dbl_expression);
    }
    public dbl_AddToSet getDbl_addtoset() {
        return dbl_addtoset;
    }

    public void setDbl_addtoset(dbl_AddToSet dbl_addtoset) {
        this.dbl_addtoset = dbl_addtoset;
    }

}