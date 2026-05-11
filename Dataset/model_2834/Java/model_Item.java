





import java.util.List;
import java.util.ArrayList;

public class model_Item extends VisibleSupport, LinkSupport, ClickSupport {

    private int width;
    private String text;
    private int height;
    private int y;
    private int x;



    public model_Item(
        int width,        String text,        int height,        int y,        int x    ) {
        super(
        );
        this.width = width;
        this.text = text;
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
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
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