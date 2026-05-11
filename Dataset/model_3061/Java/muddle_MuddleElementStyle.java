





import java.util.List;
import java.util.ArrayList;

public class muddle_MuddleElementStyle  {

    private int labelFontSize;
    private float borderWidth;
    private String shape;
    private float x;
    private float width;
    private float y;
    private String color;
    private float height;





    private muddle_MuddleElement muddle_muddleelement;


    public muddle_MuddleElementStyle(
        int labelFontSize,        float borderWidth,        String shape,        float x,        float width,        float y,        String color,        float height    ) {
        this.labelFontSize = labelFontSize;
        this.borderWidth = borderWidth;
        this.shape = shape;
        this.x = x;
        this.width = width;
        this.y = y;
        this.color = color;
        this.height = height;
    }


    public int getLabelfontsize() {
        return labelFontSize;
    }

    public void setLabelfontsize(int labelFontSize) {
        this.labelFontSize = labelFontSize;
    }
    public float getBorderwidth() {
        return borderWidth;
    }

    public void setBorderwidth(float borderWidth) {
        this.borderWidth = borderWidth;
    }
    public String getShape() {
        return shape;
    }

    public void setShape(String shape) {
        this.shape = shape;
    }
    public float getX() {
        return x;
    }

    public void setX(float x) {
        this.x = x;
    }
    public float getWidth() {
        return width;
    }

    public void setWidth(float width) {
        this.width = width;
    }
    public float getY() {
        return y;
    }

    public void setY(float y) {
        this.y = y;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }
    public float getHeight() {
        return height;
    }

    public void setHeight(float height) {
        this.height = height;
    }

    public muddle_MuddleElement getMuddle_muddleelement() {
        return muddle_muddleelement;
    }

    public void setMuddle_muddleelement(muddle_MuddleElement muddle_muddleelement) {
        this.muddle_muddleelement = muddle_muddleelement;
    }

}