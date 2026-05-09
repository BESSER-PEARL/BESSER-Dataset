





import java.util.List;
import java.util.ArrayList;

public class graph_GEdgePlacement  {

    private String side;
    private String position;
    private String offset;
    private boolean rotate;





    private graph_GEdgeLayoutable graph_gedgelayoutable;


    public graph_GEdgePlacement(
        String side,        String position,        String offset,        boolean rotate    ) {
        this.side = side;
        this.position = position;
        this.offset = offset;
        this.rotate = rotate;
    }


    public String getSide() {
        return side;
    }

    public void setSide(String side) {
        this.side = side;
    }
    public String getPosition() {
        return position;
    }

    public void setPosition(String position) {
        this.position = position;
    }
    public String getOffset() {
        return offset;
    }

    public void setOffset(String offset) {
        this.offset = offset;
    }
    public boolean getRotate() {
        return rotate;
    }

    public void setRotate(boolean rotate) {
        this.rotate = rotate;
    }

    public graph_GEdgeLayoutable getGraph_gedgelayoutable() {
        return graph_gedgelayoutable;
    }

    public void setGraph_gedgelayoutable(graph_GEdgeLayoutable graph_gedgelayoutable) {
        this.graph_gedgelayoutable = graph_gedgelayoutable;
    }

}