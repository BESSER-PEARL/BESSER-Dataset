





import java.util.List;
import java.util.ArrayList;

public class EdgeGraphics  {






    private PNML_Position pnml_position;




    private PNML_Arc pnml_arc;




    private PNML_Fill pnml_fill;




    private PNML_Line pnml_line;


    public EdgeGraphics(
    ) {
    }



    public PNML_Position getPnml_position() {
        return pnml_position;
    }

    public void setPnml_position(PNML_Position pnml_position) {
        this.pnml_position = pnml_position;
    }
    public PNML_Arc getPnml_arc() {
        return pnml_arc;
    }

    public void setPnml_arc(PNML_Arc pnml_arc) {
        this.pnml_arc = pnml_arc;
    }
    public PNML_Fill getPnml_fill() {
        return pnml_fill;
    }

    public void setPnml_fill(PNML_Fill pnml_fill) {
        this.pnml_fill = pnml_fill;
    }
    public PNML_Line getPnml_line() {
        return pnml_line;
    }

    public void setPnml_line(PNML_Line pnml_line) {
        this.pnml_line = pnml_line;
    }

}