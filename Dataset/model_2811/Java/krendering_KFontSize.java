





import java.util.List;
import java.util.ArrayList;

public class krendering_KFontSize extends KStyle {

    private boolean scaleWithZoom;
    private int size;



    public krendering_KFontSize(
        boolean scaleWithZoom,        int size    ) {
        super(
        );
        this.scaleWithZoom = scaleWithZoom;
        this.size = size;
    }


    public boolean getScalewithzoom() {
        return scaleWithZoom;
    }

    public void setScalewithzoom(boolean scaleWithZoom) {
        this.scaleWithZoom = scaleWithZoom;
    }
    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }


}