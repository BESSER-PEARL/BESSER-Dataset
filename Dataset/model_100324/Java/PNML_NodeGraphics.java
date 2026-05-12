





import java.util.List;
import java.util.ArrayList;

public class PNML_NodeGraphics extends Graphics {






    private Node node;




    private Fill fill;




    private Dimension dimension;




    private Position position;




    private Line line;


    public PNML_NodeGraphics(
    ) {
        super(
        );
    }



    public Node getNode() {
        return node;
    }

    public void setNode(Node node) {
        this.node = node;
    }
    public Fill getFill() {
        return fill;
    }

    public void setFill(Fill fill) {
        this.fill = fill;
    }
    public Dimension getDimension() {
        return dimension;
    }

    public void setDimension(Dimension dimension) {
        this.dimension = dimension;
    }
    public Position getPosition() {
        return position;
    }

    public void setPosition(Position position) {
        this.position = position;
    }
    public Line getLine() {
        return line;
    }

    public void setLine(Line line) {
        this.line = line;
    }

}