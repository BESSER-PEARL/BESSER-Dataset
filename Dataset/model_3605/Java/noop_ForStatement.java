





import java.util.List;
import java.util.ArrayList;

public class noop_ForStatement extends Statement {

    private String name;





    private noop_Expression noop_expression;




    private List<noop_Variable> noop_variables;




    private List<noop_Expression> noop_expressions;




    private List<noop_Expression> noop_expressions;


    public noop_ForStatement(
        String name    ) {
        super(
        );
        this.name = name;
        this.noop_variables = new ArrayList<>();
        this.noop_expressions = new ArrayList<>();
        this.noop_expressions = new ArrayList<>();
    }

    public noop_ForStatement(
        String name        ArrayList<noop_Variable> noop_variables,        ArrayList<noop_Expression> noop_expressions,        ArrayList<noop_Expression> noop_expressions    ) {
        this.name = name;
        this.noop_variables = noop_variables;
        this.noop_expressions = noop_expressions;
        this.noop_expressions = noop_expressions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public noop_Expression getNoop_expression() {
        return noop_expression;
    }

    public void setNoop_expression(noop_Expression noop_expression) {
        this.noop_expression = noop_expression;
    }
    public List<noop_Variable> getNoop_variables() {
        return noop_variables;
    }

    public void addNoop_variable(Noop_variable noop_variable) {
        this.noop_variables.add(noop_variable);
    }
    public List<noop_Expression> getNoop_expressions() {
        return noop_expressions;
    }

    public void addNoop_expression(Noop_expression noop_expression) {
        this.noop_expressions.add(noop_expression);
    }
    public List<noop_Expression> getNoop_expressions() {
        return noop_expressions;
    }

    public void addNoop_expression(Noop_expression noop_expression) {
        this.noop_expressions.add(noop_expression);
    }

}