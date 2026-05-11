





import java.util.List;
import java.util.ArrayList;

public class model_Arrow extends LineStyleSupport, Widget, ColorForegroundSupport, AnnotationSupport {

    private boolean left;
    private boolean right;
    private String direction;



    public model_Arrow(
        boolean left,        boolean right,        String direction    ) {
        super(
        );
        this.left = left;
        this.right = right;
        this.direction = direction;
    }


    public boolean getLeft() {
        return left;
    }

    public void setLeft(boolean left) {
        this.left = left;
    }
    public boolean getRight() {
        return right;
    }

    public void setRight(boolean right) {
        this.right = right;
    }
    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }


}