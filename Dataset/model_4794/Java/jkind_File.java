





import java.util.List;
import java.util.ArrayList;

public class jkind_File  {






    private List<jkind_Function> jkind_functions;




    private List<jkind_Node> jkind_nodes;




    private List<jkind_Constant> jkind_constants;


    public jkind_File(
    ) {
        this.jkind_functions = new ArrayList<>();
        this.jkind_nodes = new ArrayList<>();
        this.jkind_constants = new ArrayList<>();
    }

    public jkind_File(
        ArrayList<jkind_Function> jkind_functions,        ArrayList<jkind_Node> jkind_nodes,        ArrayList<jkind_Constant> jkind_constants    ) {
        this.jkind_functions = jkind_functions;
        this.jkind_nodes = jkind_nodes;
        this.jkind_constants = jkind_constants;
    }


    public List<jkind_Function> getJkind_functions() {
        return jkind_functions;
    }

    public void addJkind_function(Jkind_function jkind_function) {
        this.jkind_functions.add(jkind_function);
    }
    public List<jkind_Node> getJkind_nodes() {
        return jkind_nodes;
    }

    public void addJkind_node(Jkind_node jkind_node) {
        this.jkind_nodes.add(jkind_node);
    }
    public List<jkind_Constant> getJkind_constants() {
        return jkind_constants;
    }

    public void addJkind_constant(Jkind_constant jkind_constant) {
        this.jkind_constants.add(jkind_constant);
    }

}