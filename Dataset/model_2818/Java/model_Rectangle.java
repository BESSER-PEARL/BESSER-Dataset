





import java.util.List;
import java.util.ArrayList;

public class model_Rectangle extends ConnectableElement {

    private boolean square;
    private boolean rectangle;



    public model_Rectangle(
        boolean square,        boolean rectangle    ) {
        super(
        );
        this.square = square;
        this.rectangle = rectangle;
    }


    public boolean getSquare() {
        return square;
    }

    public void setSquare(boolean square) {
        this.square = square;
    }
    public boolean getRectangle() {
        return rectangle;
    }

    public void setRectangle(boolean rectangle) {
        this.rectangle = rectangle;
    }


}