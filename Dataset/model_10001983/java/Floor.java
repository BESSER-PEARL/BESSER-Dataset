





import java.util.List;
import java.util.ArrayList;

public class Floor  {

    private int TOP;
    private int number;
    private None box;
    private int LOCATION;
    private int BOTTOM;



    public Floor(
        int TOP,        int number,        None box,        int LOCATION,        int BOTTOM    ) {
        this.TOP = TOP;
        this.number = number;
        this.box = box;
        this.LOCATION = LOCATION;
        this.BOTTOM = BOTTOM;
    }


    public int getTop() {
        return TOP;
    }

    public void setTop(int TOP) {
        this.TOP = TOP;
    }
    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }
    public None getBox() {
        return box;
    }

    public void setBox(None box) {
        this.box = box;
    }
    public int getLocation() {
        return LOCATION;
    }

    public void setLocation(int LOCATION) {
        this.LOCATION = LOCATION;
    }
    public int getBottom() {
        return BOTTOM;
    }

    public void setBottom(int BOTTOM) {
        this.BOTTOM = BOTTOM;
    }


}