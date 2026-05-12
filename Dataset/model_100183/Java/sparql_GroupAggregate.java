





import java.util.List;
import java.util.ArrayList;

public class sparql_GroupAggregate extends Aggregate {

    private boolean isDistinct;
    private String value;





    private List<sparql_Expression> sparql_expressions;


    public sparql_GroupAggregate(
        boolean isDistinct,        String value    ) {
        super(
        );
        this.isDistinct = isDistinct;
        this.value = value;
        this.sparql_expressions = new ArrayList<>();
    }

    public sparql_GroupAggregate(
        boolean isDistinct,        String value        ArrayList<sparql_Expression> sparql_expressions    ) {
        this.isDistinct = isDistinct;
        this.value = value;
        this.sparql_expressions = sparql_expressions;
    }

    public boolean getIsdistinct() {
        return isDistinct;
    }

    public void setIsdistinct(boolean isDistinct) {
        this.isDistinct = isDistinct;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public List<sparql_Expression> getSparql_expressions() {
        return sparql_expressions;
    }

    public void addSparql_expression(Sparql_expression sparql_expression) {
        this.sparql_expressions.add(sparql_expression);
    }

}