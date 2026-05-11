





import java.util.List;
import java.util.ArrayList;

public class jkind_VariableGroup  {






    private jkind_Node jkind_node;




    private jkind_Type jkind_type;




    private jkind_Node jkind_node;




    private List<jkind_Variable> jkind_variables;




    private jkind_Node jkind_node;


    public jkind_VariableGroup(
    ) {
        this.jkind_variables = new ArrayList<>();
    }

    public jkind_VariableGroup(
        ArrayList<jkind_Variable> jkind_variables    ) {
        this.jkind_variables = jkind_variables;
    }


    public jkind_Node getJkind_node() {
        return jkind_node;
    }

    public void setJkind_node(jkind_Node jkind_node) {
        this.jkind_node = jkind_node;
    }
    public jkind_Type getJkind_type() {
        return jkind_type;
    }

    public void setJkind_type(jkind_Type jkind_type) {
        this.jkind_type = jkind_type;
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
    public jkind_Node getJkind_node() {
        return jkind_node;
    }

    public void setJkind_node(jkind_Node jkind_node) {
        this.jkind_node = jkind_node;
    }

}