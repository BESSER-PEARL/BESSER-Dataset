





import java.util.List;
import java.util.ArrayList;

public class book_Shape extends Node {

    private int lineWidth;
    private String points;



    public book_Shape(
        int lineWidth,        String points    ) {
        super(
        );
        this.lineWidth = lineWidth;
        this.points = points;
    }


    public int getLinewidth() {
        return lineWidth;
    }

    public void setLinewidth(int lineWidth) {
        this.lineWidth = lineWidth;
    }
    public String getPoints() {
        return points;
    }

    public void setPoints(String points) {
        this.points = points;
    }


}