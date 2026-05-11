





import java.util.List;
import java.util.ArrayList;

public class thingML_ExternStatement extends Action {

    private String statement;





    private List<thingML_Expression> thingml_expressions;


    public thingML_ExternStatement(
        String statement    ) {
        super(
        );
        this.statement = statement;
        this.thingml_expressions = new ArrayList<>();
    }

    public thingML_ExternStatement(
        String statement        ArrayList<thingML_Expression> thingml_expressions    ) {
        this.statement = statement;
        this.thingml_expressions = thingml_expressions;
    }

    public String getStatement() {
        return statement;
    }

    public void setStatement(String statement) {
        this.statement = statement;
    }

    public List<thingML_Expression> getThingml_expressions() {
        return thingml_expressions;
    }

    public void addThingml_expression(Thingml_expression thingml_expression) {
        this.thingml_expressions.add(thingml_expression);
    }

}