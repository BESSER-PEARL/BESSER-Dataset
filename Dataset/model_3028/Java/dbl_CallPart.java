





import java.util.List;
import java.util.ArrayList;

public class dbl_CallPart  {






    private List<dbl_Expression> dbl_expressions;




    private dbl_IdExpr dbl_idexpr;


    public dbl_CallPart(
    ) {
        this.dbl_expressions = new ArrayList<>();
    }

    public dbl_CallPart(
        ArrayList<dbl_Expression> dbl_expressions    ) {
        this.dbl_expressions = dbl_expressions;
    }


    public List<dbl_Expression> getDbl_expressions() {
        return dbl_expressions;
    }

    public void addDbl_expression(Dbl_expression dbl_expression) {
        this.dbl_expressions.add(dbl_expression);
    }
    public dbl_IdExpr getDbl_idexpr() {
        return dbl_idexpr;
    }

    public void setDbl_idexpr(dbl_IdExpr dbl_idexpr) {
        this.dbl_idexpr = dbl_idexpr;
    }

}