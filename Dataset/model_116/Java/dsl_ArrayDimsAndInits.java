





import java.util.List;
import java.util.ArrayList;

public class dsl_ArrayDimsAndInits  {

    private String squareBrackets;





    private dsl_ArrayInitializer dsl_arrayinitializer;




    private List<dsl_Expression> dsl_expressions;




    private dsl_AllocationExpression dsl_allocationexpression;


    public dsl_ArrayDimsAndInits(
        String squareBrackets    ) {
        this.squareBrackets = squareBrackets;
        this.dsl_expressions = new ArrayList<>();
    }

    public dsl_ArrayDimsAndInits(
        String squareBrackets        ArrayList<dsl_Expression> dsl_expressions    ) {
        this.squareBrackets = squareBrackets;
        this.dsl_expressions = dsl_expressions;
    }

    public String getSquarebrackets() {
        return squareBrackets;
    }

    public void setSquarebrackets(String squareBrackets) {
        this.squareBrackets = squareBrackets;
    }

    public dsl_ArrayInitializer getDsl_arrayinitializer() {
        return dsl_arrayinitializer;
    }

    public void setDsl_arrayinitializer(dsl_ArrayInitializer dsl_arrayinitializer) {
        this.dsl_arrayinitializer = dsl_arrayinitializer;
    }
    public List<dsl_Expression> getDsl_expressions() {
        return dsl_expressions;
    }

    public void addDsl_expression(Dsl_expression dsl_expression) {
        this.dsl_expressions.add(dsl_expression);
    }
    public dsl_AllocationExpression getDsl_allocationexpression() {
        return dsl_allocationexpression;
    }

    public void setDsl_allocationexpression(dsl_AllocationExpression dsl_allocationexpression) {
        this.dsl_allocationexpression = dsl_allocationexpression;
    }

}