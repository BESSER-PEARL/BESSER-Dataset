





import java.util.List;
import java.util.ArrayList;

public class ale_Call extends Expression {

    private String name;





    private ale_Expression ale_expression;




    private List<ale_Expression> ale_expressions;


    public ale_Call(
        String name    ) {
        super(
        );
        this.name = name;
        this.ale_expressions = new ArrayList<>();
    }

    public ale_Call(
        String name        ArrayList<ale_Expression> ale_expressions    ) {
        this.name = name;
        this.ale_expressions = ale_expressions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ale_Expression getAle_expression() {
        return ale_expression;
    }

    public void setAle_expression(ale_Expression ale_expression) {
        this.ale_expression = ale_expression;
    }
    public List<ale_Expression> getAle_expressions() {
        return ale_expressions;
    }

    public void addAle_expression(Ale_expression ale_expression) {
        this.ale_expressions.add(ale_expression);
    }

}