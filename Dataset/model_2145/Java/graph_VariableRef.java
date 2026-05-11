





import java.util.List;
import java.util.ArrayList;

public class graph_VariableRef extends Expr {






    private graph_Declaration graph_declaration;


    public graph_VariableRef(
    ) {
        super(
        );
    }



    public graph_Declaration getGraph_declaration() {
        return graph_declaration;
    }

    public void setGraph_declaration(graph_Declaration graph_declaration) {
        this.graph_declaration = graph_declaration;
    }

}