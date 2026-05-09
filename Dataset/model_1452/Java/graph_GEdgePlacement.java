





import java.util.List;
import java.util.ArrayList;

public class graph_GEdgePlacement  {

    private String offset;
    private String position;
    private boolean rotate;
    private String side;





    private graph_GEdgeLayoutable graph_gedgelayoutable;


    public graph_GEdgePlacement(
        String offset,        String position,        boolean rotate,        String side    ) {
        this.offset = offset;
        this.position = position;
        this.rotate = rotate;
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
    public boolean getRotate() {
        return rotate;
    }

    public void setRotate(boolean rotate) {
        this.rotate = rotate;
    }
    public String getSide() {
        return side;
    }

    public void setSide(String side) {
        this.side = side;
    }

    public graph_GEdgeLayoutable getGraph_gedgelayoutable() {
        return graph_gedgelayoutable;
    }

    public void setGraph_gedgelayoutable(graph_GEdgeLayoutable graph_gedgelayoutable) {
        this.graph_gedgelayoutable = graph_gedgelayoutable;
    }

}