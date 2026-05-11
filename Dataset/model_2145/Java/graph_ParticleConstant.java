





import java.util.List;
import java.util.ArrayList;

public class graph_ParticleConstant extends Expr {






    private graph_Vertex graph_vertex;




    private graph_Expr graph_expr;


    public graph_ParticleConstant(
    ) {
        super(
        );
    }



    public graph_Vertex getGraph_vertex() {
        return graph_vertex;
    }

    public void setGraph_vertex(graph_Vertex graph_vertex) {
        this.graph_vertex = graph_vertex;
    }
    public graph_Expr getGraph_expr() {
        return graph_expr;
    }

    public void setGraph_expr(graph_Expr graph_expr) {
        this.graph_expr = graph_expr;
    }

}