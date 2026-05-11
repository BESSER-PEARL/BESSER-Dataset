





import java.util.List;
import java.util.ArrayList;

public class SPL_FunctionCall extends LocatedElement {






    private List<SPL_Expression> spl_expressions;


    public SPL_FunctionCall(
    ) {
        super(
        );
        this.spl_expressions = new ArrayList<>();
    }

    public SPL_FunctionCall(
        ArrayList<SPL_Expression> spl_expressions    ) {
        this.spl_expressions = spl_expressions;
    }


    public List<SPL_Expression> getSpl_expressions() {
        return spl_expressions;
    }

    public void addSpl_expression(Spl_expression spl_expression) {
        this.spl_expressions.add(spl_expression);
    }

}