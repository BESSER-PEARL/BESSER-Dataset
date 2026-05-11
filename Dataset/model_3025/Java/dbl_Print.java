





import java.util.List;
import java.util.ArrayList;

public class dbl_Print extends SimpleStatement {






    private List<dbl_Expression> dbl_expressions;


    public dbl_Print(
    ) {
        super(
        );
        this.dbl_expressions = new ArrayList<>();
    }

    public dbl_Print(
        ArrayList<dbl_Expression> dbl_expressions    ) {
        this.dbl_expressions = dbl_expressions;
    }


    public List<dbl_Expression> getDbl_expressions() {
        return dbl_expressions;
    }

    public void addDbl_expression(Dbl_expression dbl_expression) {
        this.dbl_expressions.add(dbl_expression);
    }

}