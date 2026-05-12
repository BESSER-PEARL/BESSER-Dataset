





import java.util.List;
import java.util.ArrayList;

public class sparql_ExprAggArg  {

    private boolean isDistinct;





    private sparql_Expression sparql_expression;


    public sparql_ExprAggArg(
        boolean isDistinct    ) {
        this.isDistinct = isDistinct;
    }


    public boolean getIsdistinct() {
        return isDistinct;
    }

    public void setIsdistinct(boolean isDistinct) {
        this.isDistinct = isDistinct;
    }

    public sparql_Expression getSparql_expression() {
        return sparql_expression;
    }

    public void setSparql_expression(sparql_Expression sparql_expression) {
        this.sparql_expression = sparql_expression;
    }

}