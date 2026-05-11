





import java.util.List;
import java.util.ArrayList;

public class thingml_ExternStatement extends Action {

    private String statement;





    private List<thingml_Expression> thingml_expressions;


    public thingml_ExternStatement(
        String statement    ) {
        super(
        );
        this.statement = statement;
        this.thingml_expressions = new ArrayList<>();
    }

    public thingml_ExternStatement(
        String statement        ArrayList<thingml_Expression> thingml_expressions    ) {
        this.statement = statement;
        this.thingml_expressions = thingml_expressions;
    }

    public String getStatement() {
        return statement;
    }

    public void setStatement(String statement) {
        this.statement = statement;
    }

    public List<thingml_Expression> getThingml_expressions() {
        return thingml_expressions;
    }

    public void addThingml_expression(Thingml_expression thingml_expression) {
        this.thingml_expressions.add(thingml_expression);
    }

}