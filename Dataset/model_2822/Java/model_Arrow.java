





import java.util.List;
import java.util.ArrayList;

public class model_Arrow extends LineStyleSupport, ColorForegroundSupport, Widget, AnnotationSupport {

    private boolean right;
    private String direction;
    private boolean left;



    public model_Arrow(
        boolean right,        String direction,        boolean left    ) {
        super(
        );
        this.right = right;
        this.direction = direction;
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
    public boolean getLeft() {
        return left;
    }

    public void setLeft(boolean left) {
        this.left = left;
    }


}