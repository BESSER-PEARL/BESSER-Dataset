





import java.util.List;
import java.util.ArrayList;

public class gremlin_VerticesStep extends Step {

    private String vertexId;



    public gremlin_VerticesStep(
        String vertexId    ) {
        super(
        );
        this.vertexId = vertexId;
    }


    public String getVertexid() {
        return vertexId;
    }

    public void setVertexid(String vertexId) {
        this.vertexId = vertexId;
    }


}