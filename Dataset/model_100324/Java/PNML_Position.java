





import java.util.List;
import java.util.ArrayList;

public class PNML_Position extends Coordinate {






    private NodeGraphics nodegraphics;




    private EdgeGraphics edgegraphics;


    public PNML_Position(
    ) {
        super(
        );
    }



    public NodeGraphics getNodegraphics() {
        return nodegraphics;
    }

    public void setNodegraphics(NodeGraphics nodegraphics) {
        this.nodegraphics = nodegraphics;
    }
    public EdgeGraphics getEdgegraphics() {
        return edgegraphics;
    }

    public void setEdgegraphics(EdgeGraphics edgegraphics) {
        this.edgegraphics = edgegraphics;
    }

}