





import java.util.List;
import java.util.ArrayList;

public class Boat  {

    private None direction;
    private int length;
    private None startCoord;
    private int MAX_LENGTH;



    public Boat(
        None direction,        int length,        None startCoord,        int MAX_LENGTH    ) {
        this.direction = direction;
        this.length = length;
        this.startCoord = startCoord;
        this.MAX_LENGTH = MAX_LENGTH;
    }


    public None getDirection() {
        return direction;
    }

    public void setDirection(None direction) {
        this.direction = direction;
    }
    public int getLength() {
        return length;
    }

    public void setLength(int length) {
        this.length = length;
    }
    public None getStartcoord() {
        return startCoord;
    }

    public void setStartcoord(None startCoord) {
        this.startCoord = startCoord;
    }
    public int getMax_length() {
        return MAX_LENGTH;
    }

    public void setMax_length(int MAX_LENGTH) {
        this.MAX_LENGTH = MAX_LENGTH;
    }


}