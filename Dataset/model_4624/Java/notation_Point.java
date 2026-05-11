





import java.util.List;
import java.util.ArrayList;

public class notation_Point  {

    private int x;
    private int y;





    private notation_Polyline notation_polyline;


    public notation_Point(
        int x,        int y    ) {
        this.x = x;
        this.y = y;
    }


    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }
    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
    }

    public notation_Polyline getNotation_polyline() {
        return notation_polyline;
    }

    public void setNotation_polyline(notation_Polyline notation_polyline) {
        this.notation_polyline = notation_polyline;
    }

}