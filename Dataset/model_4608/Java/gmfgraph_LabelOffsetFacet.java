





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_LabelOffsetFacet extends VisualFacet {

    private int x;
    private int y;



    public gmfgraph_LabelOffsetFacet(
        int x,        int y    ) {
        super(
        );
        this.x = x;
        this.y = y;
    }


    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }
    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
    }


}