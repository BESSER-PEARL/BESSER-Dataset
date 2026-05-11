





import java.util.List;
import java.util.ArrayList;

public class mm_algorithms_GraphicsAlgorithm extends GraphicsAlgorithmContainer, styles_AbstractStyle {

    private int width;
    private int height;
    private int y;
    private int x;



    public mm_algorithms_GraphicsAlgorithm(
        int width,        int height,        int y,        int x    ) {
        super(
        );
        this.width = width;
        this.height = height;
        this.y = y;
        this.x = x;
    }


    public int getWidth() {
        return width;
    }

    public void setWidth(int width) {
        this.width = width;
    }
    public int getHeight() {
        return height;
    }

    public void setHeight(int height) {
        this.height = height;
    }
    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
    }
    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }


}