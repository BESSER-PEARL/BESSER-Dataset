





import java.util.List;
import java.util.ArrayList;

public class simpleGraph_Position extends GraphElement {

    private int X;
    private int Y;



    public simpleGraph_Position(
        int X,        int Y    ) {
        super(
        );
        this.X = X;
        this.Y = Y;
    }


    public int getX() {
        return X;
    }

    public void setX(int X) {
        this.X = X;
    }
    public int getY() {
        return Y;
    }

    public void setY(int Y) {
        this.Y = Y;
    }


}