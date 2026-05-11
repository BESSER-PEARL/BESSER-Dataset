





import java.util.List;
import java.util.ArrayList;

public class mm_algorithms_GraphicsAlgorithm extends styles_AbstractStyle, GraphicsAlgorithmContainer {

    private int x;
    private int y;
    private int width;
    private int height;





    private styles_Style styles_style;


    public mm_algorithms_GraphicsAlgorithm(
        int x,        int y,        int width,        int height    ) {
        super(
        );
        this.x = x;
        this.y = y;
        this.width = width;
        this.height = height;
    }


    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }
    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
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

    public styles_Style getStyles_style() {
        return styles_style;
    }

    public void setStyles_style(styles_Style styles_style) {
        this.styles_style = styles_style;
    }

}