





import java.util.List;
import java.util.ArrayList;

public class PNML_Position extends Coordinate {






    private EdgeGraphics edgegraphics;




    private NodeGraphics nodegraphics;


    public PNML_Position(
    ) {
        super(
        );
    }



    public EdgeGraphics getEdgegraphics() {
        return edgegraphics;
    }

    public void setEdgegraphics(EdgeGraphics edgegraphics) {
        this.edgegraphics = edgegraphics;
    }
    public NodeGraphics getNodegraphics() {
        return nodegraphics;
    }

    public void setNodegraphics(NodeGraphics nodegraphics) {
        this.nodegraphics = nodegraphics;
    }

}