





import java.util.List;
import java.util.ArrayList;

public class sparql_CountAggregate extends Aggregate {

    private boolean isDistinct;
    private boolean isAll;





    private sparql_Expression sparql_expression;


    public sparql_CountAggregate(
        boolean isDistinct,        boolean isAll    ) {
        super(
        );
        this.isDistinct = isDistinct;
        this.isAll = isAll;
    }


    public boolean getIsdistinct() {
        return isDistinct;
    }

    public void setIsdistinct(boolean isDistinct) {
        this.isDistinct = isDistinct;
    }
    public boolean getIsall() {
        return isAll;
    }

    public void setIsall(boolean isAll) {
        this.isAll = isAll;
    }

    public sparql_Expression getSparql_expression() {
        return sparql_expression;
    }

    public void setSparql_expression(sparql_Expression sparql_expression) {
        this.sparql_expression = sparql_expression;
    }

}