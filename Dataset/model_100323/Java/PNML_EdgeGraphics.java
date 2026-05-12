





import java.util.List;
import java.util.ArrayList;

public class PNML_EdgeGraphics extends Graphics {






    private Fill fill;




    private Line line;




    private List<Position> positions;


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
    public List<Position> getPositions() {
        return positions;
    }

    public void addPosition(Position position) {
        this.positions.add(position);
    }

}