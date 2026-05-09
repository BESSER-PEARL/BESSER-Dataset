





import java.util.List;
import java.util.ArrayList;

public class eaglemodel_Label  {

    private float x;
    private float y;
    private boolean xref;
    private int ratio;
    private int rot;
    private int layer;
    private float size;
    private String font;





    private eaglemodel_Segment eaglemodel_segment;


    public eaglemodel_Label(
        float x,        float y,        boolean xref,        int ratio,        int rot,        int layer,        float size,        String font    ) {
        this.x = x;
        this.y = y;
        this.xref = xref;
        this.ratio = ratio;
        this.rot = rot;
        this.layer = layer;
        this.size = size;
        this.font = font;
    }


    public float getX() {
        return x;
    }

    public void setX(float x) {
        this.x = x;
    }
    public float getY() {
        return y;
    }

    public void setY(float y) {
        this.y = y;
    }
    public boolean getXref() {
        return xref;
    }

    public void setXref(boolean xref) {
        this.xref = xref;
    }
    public int getRatio() {
        return ratio;
    }

    public void setRatio(int ratio) {
        this.ratio = ratio;
    }
    public int getRot() {
        return rot;
    }

    public void setRot(int rot) {
        this.rot = rot;
    }
    public int getLayer() {
        return layer;
    }

    public void setLayer(int layer) {
        this.layer = layer;
    }
    public float getSize() {
        return size;
    }

    public void setSize(float size) {
        this.size = size;
    }
    public String getFont() {
        return font;
    }

    public void setFont(String font) {
        this.font = font;
    }

    public eaglemodel_Segment getEaglemodel_segment() {
        return eaglemodel_segment;
    }

    public void setEaglemodel_segment(eaglemodel_Segment eaglemodel_segment) {
        this.eaglemodel_segment = eaglemodel_segment;
    }

}