





import java.util.List;
import java.util.ArrayList;

public class PNML_NodeGraphics extends Graphics {






    private Dimension dimension;




    private Position position;




    private Fill fill;




    private Line line;


    public PNML_NodeGraphics(
    ) {
        super(
        );
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
    public Fill getFill() {
        return fill;
    }

    public void setFill(Fill fill) {
        this.fill = fill;
    }
    public Line getLine() {
        return line;
    }

    public void setLine(Line line) {
        this.line = line;
    }

}