





import java.util.List;
import java.util.ArrayList;

public class ale_Let extends Expression {






    private ale_Expression ale_expression;




    private List<ale_binding> ale_bindings;


    public ale_Let(
    ) {
        super(
        );
        this.ale_bindings = new ArrayList<>();
    }

    public ale_Let(
        ArrayList<ale_binding> ale_bindings    ) {
        this.ale_bindings = ale_bindings;
    }


    public ale_Expression getAle_expression() {
        return ale_expression;
    }

    public void setAle_expression(ale_Expression ale_expression) {
        this.ale_expression = ale_expression;
    }
    public List<ale_binding> getAle_bindings() {
        return ale_bindings;
    }

    public void addAle_binding(Ale_binding ale_binding) {
        this.ale_bindings.add(ale_binding);
    }

}