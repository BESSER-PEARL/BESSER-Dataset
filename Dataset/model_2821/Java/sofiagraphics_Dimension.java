





import java.util.List;
import java.util.ArrayList;

public class sofiagraphics_Dimension  {

    private float width;
    private boolean wrelative;
    private boolean noresize;
    private float height;
    private boolean hrelative;



    public sofiagraphics_Dimension(
        float width,        boolean wrelative,        boolean noresize,        float height,        boolean hrelative    ) {
        this.width = width;
        this.wrelative = wrelative;
        this.noresize = noresize;
        this.height = height;
        this.hrelative = hrelative;
    }


    public float getWidth() {
        return width;
    }

    public void setWidth(float width) {
        this.width = width;
    }
    public boolean getWrelative() {
        return wrelative;
    }

    public void setWrelative(boolean wrelative) {
        this.wrelative = wrelative;
    }
    public boolean getNoresize() {
        return noresize;
    }

    public void setNoresize(boolean noresize) {
        this.noresize = noresize;
    }
    public float getHeight() {
        return height;
    }

    public void setHeight(float height) {
        this.height = height;
    }
    public boolean getHrelative() {
        return hrelative;
    }

    public void setHrelative(boolean hrelative) {
        this.hrelative = hrelative;
    }


}