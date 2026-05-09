





import java.util.List;
import java.util.ArrayList;

public class hlcorestructure_ArcGraphics extends Graphics {






    private hlcorestructure_Arc hlcorestructure_arc;




    private hlcorestructure_Arc hlcorestructure_arc;




    private hlcorestructure_Line hlcorestructure_line;




    private List<hlcorestructure_Position> hlcorestructure_positions;




    private hlcorestructure_Position hlcorestructure_position;




    private hlcorestructure_Line hlcorestructure_line;


    public hlcorestructure_ArcGraphics(
    ) {
        super(
        );
        this.hlcorestructure_positions = new ArrayList<>();
    }

    public hlcorestructure_ArcGraphics(
        ArrayList<hlcorestructure_Position> hlcorestructure_positions    ) {
        this.hlcorestructure_positions = hlcorestructure_positions;
    }


    public hlcorestructure_Arc getHlcorestructure_arc() {
        return hlcorestructure_arc;
    }

    public void setHlcorestructure_arc(hlcorestructure_Arc hlcorestructure_arc) {
        this.hlcorestructure_arc = hlcorestructure_arc;
    }
    public hlcorestructure_Arc getHlcorestructure_arc() {
        return hlcorestructure_arc;
    }

    public void setHlcorestructure_arc(hlcorestructure_Arc hlcorestructure_arc) {
        this.hlcorestructure_arc = hlcorestructure_arc;
    }
    public hlcorestructure_Line getHlcorestructure_line() {
        return hlcorestructure_line;
    }

    public void setHlcorestructure_line(hlcorestructure_Line hlcorestructure_line) {
        this.hlcorestructure_line = hlcorestructure_line;
    }
    public List<hlcorestructure_Position> getHlcorestructure_positions() {
        return hlcorestructure_positions;
    }

    public void addHlcorestructure_position(Hlcorestructure_position hlcorestructure_position) {
        this.hlcorestructure_positions.add(hlcorestructure_position);
    }
    public hlcorestructure_Position getHlcorestructure_position() {
        return hlcorestructure_position;
    }

    public void setHlcorestructure_position(hlcorestructure_Position hlcorestructure_position) {
        this.hlcorestructure_position = hlcorestructure_position;
    }
    public hlcorestructure_Line getHlcorestructure_line() {
        return hlcorestructure_line;
    }

    public void setHlcorestructure_line(hlcorestructure_Line hlcorestructure_line) {
        this.hlcorestructure_line = hlcorestructure_line;
    }

}