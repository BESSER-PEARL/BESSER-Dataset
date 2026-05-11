





import java.util.List;
import java.util.ArrayList;

public class jkind_Equation  {






    private jkind_Node jkind_node;




    private List<jkind_Variable> jkind_variables;




    private jkind_Expr jkind_expr;


    public jkind_Equation(
    ) {
        this.jkind_variables = new ArrayList<>();
    }

    public jkind_Equation(
        ArrayList<jkind_Variable> jkind_variables    ) {
        this.jkind_variables = jkind_variables;
    }


    public jkind_Node getJkind_node() {
        return jkind_node;
    }

    public void setJkind_node(jkind_Node jkind_node) {
        this.jkind_node = jkind_node;
    }
    public List<jkind_Variable> getJkind_variables() {
        return jkind_variables;
    }

    public void addJkind_variable(Jkind_variable jkind_variable) {
        this.jkind_variables.add(jkind_variable);
    }
    public jkind_Expr getJkind_expr() {
        return jkind_expr;
    }

    public void setJkind_expr(jkind_Expr jkind_expr) {
        this.jkind_expr = jkind_expr;
    }

}