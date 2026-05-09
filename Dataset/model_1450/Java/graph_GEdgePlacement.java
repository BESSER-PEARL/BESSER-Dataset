





import java.util.List;
import java.util.ArrayList;

public class graph_GEdgePlacement  {

    private String side;
    private String offset;
    private String position;





    private graph_GEdgeLayoutable graph_gedgelayoutable;


    public graph_GEdgePlacement(
        String side,        String offset,        String position    ) {
        this.side = side;
        this.offset = offset;
        this.position = position;
    }


    public String getSide() {
        return side;
    }

    public void setSide(String side) {
        this.side = side;
    }
    public String getOffset() {
        return offset;
    }

    public void setOffset(String offset) {
        this.offset = offset;
    }
    public String getPosition() {
        return position;
    }

    public void setPosition(String position) {
        this.position = position;
    }

    public graph_GEdgeLayoutable getGraph_gedgelayoutable() {
        return graph_gedgelayoutable;
    }

    public void setGraph_gedgelayoutable(graph_GEdgeLayoutable graph_gedgelayoutable) {
        this.graph_gedgelayoutable = graph_gedgelayoutable;
    }

}