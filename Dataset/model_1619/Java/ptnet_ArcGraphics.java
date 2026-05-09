





import java.util.List;
import java.util.ArrayList;

public class ptnet_ArcGraphics extends Graphics {






    private ptnet_Position ptnet_position;




    private ptnet_Arc ptnet_arc;




    private List<ptnet_Position> ptnet_positions;




    private ptnet_Line ptnet_line;




    private ptnet_Line ptnet_line;




    private ptnet_Arc ptnet_arc;


    public ptnet_ArcGraphics(
    ) {
        super(
        );
        this.ptnet_positions = new ArrayList<>();
    }

    public ptnet_ArcGraphics(
        ArrayList<ptnet_Position> ptnet_positions    ) {
        this.ptnet_positions = ptnet_positions;
    }


    public ptnet_Position getPtnet_position() {
        return ptnet_position;
    }

    public void setPtnet_position(ptnet_Position ptnet_position) {
        this.ptnet_position = ptnet_position;
    }
    public ptnet_Arc getPtnet_arc() {
        return ptnet_arc;
    }

    public void setPtnet_arc(ptnet_Arc ptnet_arc) {
        this.ptnet_arc = ptnet_arc;
    }
    public List<ptnet_Position> getPtnet_positions() {
        return ptnet_positions;
    }

    public void addPtnet_position(Ptnet_position ptnet_position) {
        this.ptnet_positions.add(ptnet_position);
    }
    public ptnet_Line getPtnet_line() {
        return ptnet_line;
    }

    public void setPtnet_line(ptnet_Line ptnet_line) {
        this.ptnet_line = ptnet_line;
    }
    public ptnet_Line getPtnet_line() {
        return ptnet_line;
    }

    public void setPtnet_line(ptnet_Line ptnet_line) {
        this.ptnet_line = ptnet_line;
    }
    public ptnet_Arc getPtnet_arc() {
        return ptnet_arc;
    }

    public void setPtnet_arc(ptnet_Arc ptnet_arc) {
        this.ptnet_arc = ptnet_arc;
    }

}