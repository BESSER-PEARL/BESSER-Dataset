





import java.util.List;
import java.util.ArrayList;

public class model_Arrow extends Widget, LineStyleSupport, ColorForegroundSupport, AnnotationSupport {

    private String direction;
    private boolean right;
    private boolean left;



    public model_Arrow(
        String direction,        boolean right,        boolean left    ) {
        super(
        );
        this.direction = direction;
        this.right = right;
        this.left = left;
    }


    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }
    public boolean getRight() {
        return right;
    }

    public void setRight(boolean right) {
        this.right = right;
    }
    public boolean getLeft() {
        return left;
    }

    public void setLeft(boolean left) {
        this.left = left;
    }


}