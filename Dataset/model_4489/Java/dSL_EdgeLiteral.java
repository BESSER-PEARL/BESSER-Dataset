





import java.util.List;
import java.util.ArrayList;

public class dSL_EdgeLiteral extends Expression {

    private String edge;



    public dSL_EdgeLiteral(
        String edge    ) {
        super(
        );
        this.edge = edge;
    }


    public String getEdge() {
        return edge;
    }

    public void setEdge(String edge) {
        this.edge = edge;
    }


}