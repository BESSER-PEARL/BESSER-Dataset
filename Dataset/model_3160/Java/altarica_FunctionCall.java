





import java.util.List;
import java.util.ArrayList;

public class altarica_FunctionCall extends Expression {

    private String name;





    private List<altarica_Expression> altarica_expressions;


    public altarica_FunctionCall(
        String name    ) {
        super(
        );
        this.name = name;
        this.altarica_expressions = new ArrayList<>();
    }

    public altarica_FunctionCall(
        String name        ArrayList<altarica_Expression> altarica_expressions    ) {
        this.name = name;
        this.altarica_expressions = altarica_expressions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<altarica_Expression> getAltarica_expressions() {
        return altarica_expressions;
    }

    public void addAltarica_expression(Altarica_expression altarica_expression) {
        this.altarica_expressions.add(altarica_expression);
    }

}