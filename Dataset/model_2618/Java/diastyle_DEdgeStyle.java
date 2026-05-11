





import java.util.List;
import java.util.ArrayList;

public class diastyle_DEdgeStyle extends DNodeEdgeStyle {

    private String arrowDirection;
    private String shape;
    private int arrowSize;



    public diastyle_DEdgeStyle(
        String arrowDirection,        String shape,        int arrowSize    ) {
        super(
        );
        this.arrowDirection = arrowDirection;
        this.shape = shape;
        this.arrowSize = arrowSize;
    }


    public String getArrowdirection() {
        return arrowDirection;
    }

    public void setArrowdirection(String arrowDirection) {
        this.arrowDirection = arrowDirection;
    }
    public String getShape() {
        return shape;
    }

    public void setShape(String shape) {
        this.shape = shape;
    }
    public int getArrowsize() {
        return arrowSize;
    }

    public void setArrowsize(int arrowSize) {
        this.arrowSize = arrowSize;
    }


}