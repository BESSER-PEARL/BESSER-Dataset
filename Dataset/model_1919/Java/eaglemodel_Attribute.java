





import java.util.List;
import java.util.ArrayList;

public class eaglemodel_Attribute  {

    private int rot;
    private boolean constant;
    private int layer;
    private String display;
    private String value;
    private String font;
    private float x;
    private float size;
    private String name;
    private float y;
    private int ratio;



    public eaglemodel_Attribute(
        int rot,        boolean constant,        int layer,        String display,        String value,        String font,        float x,        float size,        String name,        float y,        int ratio    ) {
        this.rot = rot;
        this.constant = constant;
        this.layer = layer;
        this.display = display;
        this.value = value;
        this.font = font;
        this.x = x;
        this.size = size;
        this.name = name;
        this.y = y;
        this.ratio = ratio;
    }


    public int getRot() {
        return rot;
    }

    public void setRot(int rot) {
        this.rot = rot;
    }
    public boolean getConstant() {
        return constant;
    }

    public void setConstant(boolean constant) {
        this.constant = constant;
    }
    public int getLayer() {
        return layer;
    }

    public void setLayer(int layer) {
        this.layer = layer;
    }
    public String getDisplay() {
        return display;
    }

    public void setDisplay(String display) {
        this.display = display;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getFont() {
        return font;
    }

    public void setFont(String font) {
        this.font = font;
    }
    public float getX() {
        return x;
    }

    public void setX(float x) {
        this.x = x;
    }
    public float getSize() {
        return size;
    }

    public void setSize(float size) {
        this.size = size;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public float getY() {
        return y;
    }

    public void setY(float y) {
        this.y = y;
    }
    public int getRatio() {
        return ratio;
    }

    public void setRatio(int ratio) {
        this.ratio = ratio;
    }


}