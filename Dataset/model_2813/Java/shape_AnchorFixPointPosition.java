





import java.util.List;
import java.util.ArrayList;

public class shape_AnchorFixPointPosition extends AnchorPositionPos {

    private int ycor;
    private int xcor;



    public shape_AnchorFixPointPosition(
        int ycor,        int xcor    ) {
        super(
        );
        this.ycor = ycor;
        this.xcor = xcor;
    }


    public int getYcor() {
        return ycor;
    }

    public void setYcor(int ycor) {
        this.ycor = ycor;
    }
    public int getXcor() {
        return xcor;
    }

    public void setXcor(int xcor) {
        this.xcor = xcor;
    }


}