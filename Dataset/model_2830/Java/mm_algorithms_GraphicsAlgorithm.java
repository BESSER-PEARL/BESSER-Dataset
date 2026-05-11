





import java.util.List;
import java.util.ArrayList;

public class mm_algorithms_GraphicsAlgorithm extends GraphicsAlgorithmContainer, styles_AbstractStyle {

    private int x;
    private int height;
    private int y;
    private int width;





    private styles_Style styles_style;


    public mm_algorithms_GraphicsAlgorithm(
        int x,        int height,        int y,        int width    ) {
        super(
        );
        this.x = x;
        this.height = height;
        this.y = y;
        this.width = width;
    }


    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
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
    public int getWidth() {
        return width;
    }

    public void setWidth(int width) {
        this.width = width;
    }

    public styles_Style getStyles_style() {
        return styles_style;
    }

    public void setStyles_style(styles_Style styles_style) {
        this.styles_style = styles_style;
    }

}