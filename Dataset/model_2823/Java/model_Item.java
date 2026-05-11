





import java.util.List;
import java.util.ArrayList;

public class model_Item extends LinkSupport {

    private int y;
    private int width;
    private String text;
    private int x;
    private int height;



    public model_Item(
        int y,        int width,        String text,        int x,        int height    ) {
        super(
        );
        this.y = y;
        this.width = width;
        this.text = text;
        this.x = x;
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
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
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


}