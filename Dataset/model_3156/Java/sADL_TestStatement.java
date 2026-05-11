





import java.util.List;
import java.util.ArrayList;

public class sADL_TestStatement extends ExpressionScope {






    private List<sADL_Expression> sadl_expressions;


    public sADL_TestStatement(
    ) {
        super(
        );
        this.sadl_expressions = new ArrayList<>();
    }

    public sADL_TestStatement(
        ArrayList<sADL_Expression> sadl_expressions    ) {
        this.sadl_expressions = sadl_expressions;
    }


    public List<sADL_Expression> getSadl_expressions() {
        return sadl_expressions;
    }

    public void addSadl_expression(Sadl_expression sadl_expression) {
        this.sadl_expressions.add(sadl_expression);
    }

}