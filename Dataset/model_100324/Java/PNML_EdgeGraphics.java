





import java.util.List;
import java.util.ArrayList;

public class PNML_EdgeGraphics extends Graphics {






    private List<Position> positions;




    private Arc arc;




    private Line line;




    private Fill fill;


    public PNML_EdgeGraphics(
    ) {
        super(
        );
        this.positions = new ArrayList<>();
    }

    public PNML_EdgeGraphics(
        ArrayList<Position> positions    ) {
        this.positions = positions;
    }


    public List<Position> getPositions() {
        return positions;
    }

    public void addPosition(Position position) {
        this.positions.add(position);
    }
    public Arc getArc() {
        return arc;
    }

    public void setArc(Arc arc) {
        this.arc = arc;
    }
    public Line getLine() {
        return line;
    }

    public void setLine(Line line) {
        this.line = line;
    }
    public Fill getFill() {
        return fill;
    }

    public void setFill(Fill fill) {
        this.fill = fill;
    }

}