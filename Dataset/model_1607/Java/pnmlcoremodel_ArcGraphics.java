





import java.util.List;
import java.util.ArrayList;

public class pnmlcoremodel_ArcGraphics extends Graphics {






    private pnmlcoremodel_Arc pnmlcoremodel_arc;




    private List<pnmlcoremodel_Position> pnmlcoremodel_positions;




    private pnmlcoremodel_Arc pnmlcoremodel_arc;




    private pnmlcoremodel_Position pnmlcoremodel_position;


    public pnmlcoremodel_ArcGraphics(
    ) {
        super(
        );
        this.pnmlcoremodel_positions = new ArrayList<>();
    }

    public pnmlcoremodel_ArcGraphics(
        ArrayList<pnmlcoremodel_Position> pnmlcoremodel_positions    ) {
        this.pnmlcoremodel_positions = pnmlcoremodel_positions;
    }


    public pnmlcoremodel_Arc getPnmlcoremodel_arc() {
        return pnmlcoremodel_arc;
    }

    public void setPnmlcoremodel_arc(pnmlcoremodel_Arc pnmlcoremodel_arc) {
        this.pnmlcoremodel_arc = pnmlcoremodel_arc;
    }
    public List<pnmlcoremodel_Position> getPnmlcoremodel_positions() {
        return pnmlcoremodel_positions;
    }

    public void addPnmlcoremodel_position(Pnmlcoremodel_position pnmlcoremodel_position) {
        this.pnmlcoremodel_positions.add(pnmlcoremodel_position);
    }
    public pnmlcoremodel_Arc getPnmlcoremodel_arc() {
        return pnmlcoremodel_arc;
    }

    public void setPnmlcoremodel_arc(pnmlcoremodel_Arc pnmlcoremodel_arc) {
        this.pnmlcoremodel_arc = pnmlcoremodel_arc;
    }
    public pnmlcoremodel_Position getPnmlcoremodel_position() {
        return pnmlcoremodel_position;
    }

    public void setPnmlcoremodel_position(pnmlcoremodel_Position pnmlcoremodel_position) {
        this.pnmlcoremodel_position = pnmlcoremodel_position;
    }

}