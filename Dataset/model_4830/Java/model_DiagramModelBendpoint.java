





import java.util.List;
import java.util.ArrayList;

public class model_DiagramModelBendpoint extends Cloneable {

    private int endX;
    private int startY;
    private int startX;
    private int endY;



    public model_DiagramModelBendpoint(
        int endX,        int startY,        int startX,        int endY    ) {
        super(
        );
        this.endX = endX;
        this.startY = startY;
        this.startX = startX;
        this.endY = endY;
    }


    public int getEndx() {
        return endX;
    }

    public void setEndx(int endX) {
        this.endX = endX;
    }
    public int getStarty() {
        return startY;
    }

    public void setStarty(int startY) {
        this.startY = startY;
    }
    public int getStartx() {
        return startX;
    }

    public void setStartx(int startX) {
        this.startX = startX;
    }
    public int getEndy() {
        return endY;
    }

    public void setEndy(int endY) {
        this.endY = endY;
    }


}