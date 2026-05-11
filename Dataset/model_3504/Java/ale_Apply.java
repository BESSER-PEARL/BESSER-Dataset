





import java.util.List;
import java.util.ArrayList;

public class ale_Apply extends Expression {

    private String varName;
    private String name;





    private ale_typeLiteral ale_typeliteral;




    private ale_Expression ale_expression;




    private ale_Expression ale_expression;




    private List<ale_Expression> ale_expressions;


    public ale_Apply(
        String varName,        String name    ) {
        super(
        );
        this.varName = varName;
        this.name = name;
        this.ale_expressions = new ArrayList<>();
    }

    public ale_Apply(
        String varName,        String name        ArrayList<ale_Expression> ale_expressions    ) {
        this.varName = varName;
        this.name = name;
        this.ale_expressions = ale_expressions;
    }

    public String getVarname() {
        return varName;
    }

    public void setVarname(String varName) {
        this.varName = varName;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ale_typeLiteral getAle_typeliteral() {
        return ale_typeliteral;
    }

    public void setAle_typeliteral(ale_typeLiteral ale_typeliteral) {
        this.ale_typeliteral = ale_typeliteral;
    }
    public ale_Expression getAle_expression() {
        return ale_expression;
    }

    public void setAle_expression(ale_Expression ale_expression) {
        this.ale_expression = ale_expression;
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